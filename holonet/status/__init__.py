# -*- coding: utf8 -*-

import socket
from urllib.parse import urlparse
from builtins import ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError

from elasticsearch import ConnectionError
from celery import task
from omnibus.exceptions import OmnibusPublisherException, OmnibusException
from omnibus.settings import PUBLISHER_ADDRESS

from django.conf import settings
from django.core.cache import cache

from holonet.core.elasticsearch import get_connection, index_check
from holonet.core.omnibus import publish


@task
def test_task():
    return True


class BaseStatusClass(object):

    @property
    def name(self):
        """
        Needs to be valid in a url!
        """
        raise NotImplementedError('Please add the name property.')

    STATUSES = (
        (0, 'Not Responding'),
        (1, 'Ready'),
        (2, 'Unknown'),
    )

    @property
    def status(self):
        raise NotImplementedError('Please implement the status function.')


class ElasticsearchStatus(BaseStatusClass):

    name = 'elasticsearch'

    def status(self):
        try:
            connection = get_connection()
            index_check()

            health = connection.cluster.health(index=settings.INDEX_NAME)

            return bool(health['status'] in ['green', 'yellow'])

        except (ConnectionError, OSError):
            return False


class CacheStatus(BaseStatusClass):

    name = 'cache'

    def status(self):
        cache.set('test_key', 'test', 30)

        value = cache.get('test_key')
        return bool(value)


class CeleryStatus(BaseStatusClass):

    name = 'celery'

    def status(self):
        result = test_task.delay()
        return not result.failed()


class WebSocketsStatus(BaseStatusClass):

    name = 'websockets'

    def status(self):
        try:
            publish(
                'test_channel',
                'test',
                {'text': 'test message'},
                sender='test_server'
            )
        except (OmnibusPublisherException, OmnibusException):
            return False

        try:
            socket_connection = socket.socket()
            parser = urlparse(PUBLISHER_ADDRESS)
            socket_connection.connect((parser.hostname, parser.port))
            socket_connection.close()
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            return False

        return True


class PolicyServiceStatus(BaseStatusClass):

    name = 'policyservice'

    def status(self):
        response = ''
        try:
            socket_connection = socket.socket()
            parser = urlparse(settings.POLICYSERVICE_URL)
            socket_connection.connect((parser.hostname, parser.port))
            socket_connection.send(('recipient=bwoeuhwfihewfcn@%s\n' % settings.MASTER_DOMAIN)
                                   .encode())
            response = (socket_connection.recv(1024)).decode("utf-8")
            socket_connection.close()
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            return False

        return bool(response.strip() == 'action=REJECT Address does not exist')


class PostfixStatus(BaseStatusClass):

    name = 'postfix'

    def status(self):
        header = ''
        try:
            socket_connection = socket.socket()
            parser = urlparse(settings.POSTFIX_URL)
            socket_connection.connect((parser.hostname, parser.port))
            header = (socket_connection.recv(1024)).decode("utf-8")
            socket_connection.close()
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            return False

        return header.startswith('220')
