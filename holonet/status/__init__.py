# -*- coding: utf8 -*-

from redis.exceptions import ConnectionError as RedisConnectionError
import socket
import json
from urllib.parse import urlparse
from builtins import ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError

from elasticsearch import ConnectionError
from celery import task

from django.conf import settings
from django.core.cache import cache

from holonet.core.elasticsearch import get_connection, index_check
from holonet.core.management.commands.sasl_authentication import Handler
from holonet.core.management.commands.outgoing_policy import Handler as OutgoingHandler


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
        try:
            result = test_task.delay()
            return not result.failed()
        except (OSError, RedisConnectionError):
            return False


class PolicyServiceStatus(BaseStatusClass):

    name = 'policyservice'

    def status(self):
        try:
            parser = urlparse(settings.INCOMING_SOCKET_LOCATION)
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.connect((parser.hostname, parser.port))
            socket_connection.send(('recipient=bwoeuhwfihewfcn@%s\n' %
                                    settings.MASTER_DOMAIN).encode())
            response = (socket_connection.recv(1024)).decode()
            socket_connection.close()
            incoming_result = bool(response.strip() == 'action=REJECT Address does not exist')

            parser = urlparse(settings.OUTGOING_SOCKET_LOCATION)
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.connect((parser.hostname, parser.port))
            socket_connection.send('test=1\n'.encode())
            response = (socket_connection.recv(1024)).decode()
            socket_connection.close()
            outgoing_result = bool(response.strip().
                                   startswith('action=%s' % OutgoingHandler.TEST_RESPONSE))

        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, OSError):
            return False

        return bool(incoming_result and outgoing_result)


class SASLServiceStatus(BaseStatusClass):

    name = 'saslservice'

    def status(self):
        try:
            socket_connection = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            socket_connection.connect(settings.SASL_SOCKET_LOCATION)
            socket_connection.send('H2\t0\t0\tholonet\nTholonet/test'.encode())
            response = (socket_connection.recv(1024)).decode()
            socket_connection.close()
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError,
                OSError):
            return False

        return bool(response.strip() == '%s%s' % (
            Handler.DICT_PROTOCOL_HOLONET_TEST_RESPONSE,
            json.dumps({'content': 'holonet/test'})
        ))


class PostfixStatus(BaseStatusClass):

    name = 'postfix'

    def status(self):
        try:
            socket_connection = socket.socket()
            parser = urlparse(settings.POSTFIX_URL)
            socket_connection.connect((parser.hostname, parser.port))
            header = (socket_connection.recv(1024)).decode("utf-8")
            socket_connection.close()
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            return False

        return header.startswith('220')
