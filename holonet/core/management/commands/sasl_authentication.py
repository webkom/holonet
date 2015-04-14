# -*- coding: utf8 -*-

import json
import logging

from django.conf import settings
from django.contrib.auth import authenticate
from . import SocketCommand, BaseDovecotSASLHandler


sasl_logger = logging.getLogger('holonet.sasl_authentication')


class Handler(object):
    DICT_PROTOCOL_CMD_HELLO = 'H'
    DICT_PROTOCOL_CMD_LOOKUP = 'L'

    DICT_PROTOCOL_REPLY_OK = 'O'
    DICT_PROTOCOL_REPLY_NOTFOUND = 'N'
    DICT_PROTOCOL_REPLY_FAIL = 'F'

    DICT_PROTOCOL_HOLONET_TEST_RESPONSE = 'T'

    def success(self, payload):
        return "%s%s" % (self.DICT_PROTOCOL_REPLY_OK, json.dumps(payload))

    def not_found(self):
        return self.DICT_PROTOCOL_REPLY_NOTFOUND

    def failure(self):
        return self.DICT_PROTOCOL_REPLY_FAIL

    def test(self, payload):
        return "%s%s" % (self.DICT_PROTOCOL_HOLONET_TEST_RESPONSE, json.dumps(payload))

    def userdb_payload(self):
        return {
            'home': settings.SASL_LUSER_HOME,
            'uid': settings.SASL_LUSER_UID,
            'gid': settings.SASL_LUSER_GID
        }

    def passdb_payload(self, password):
        return {
            'password': password,
            'userdb_home': settings.SASL_LUSER_HOME,
            'userdb_uid': settings.SASL_LUSER_UID,
            'userdb_gid': settings.SASL_LUSER_GID
        }

    def consider(self, params):
        for line in params:

            if len(line) < 3:
                break

            start_character = line[0]
            line_payload = line[1:]

            if start_character == self.DICT_PROTOCOL_CMD_HELLO:
                # We assume the hello message is valid, do nothing
                pass

            elif start_character == self.DICT_PROTOCOL_CMD_LOOKUP:

                try:
                    namespace, query_database, login, password = line_payload.split('/')
                    sasl_logger.info(
                        'Lookup received and parsed: %s/%s/%s/*****' %
                        (namespace, query_database, login)
                    )
                except ValueError:
                    sasl_logger.error(
                        'Lookup received but could not parse it: %s' % line_payload,
                        extra={
                            'payload': line_payload
                        }
                    )
                    break

                if namespace == 'shared':
                    if query_database == 'passdb':
                        login_split = login.split('@')

                        username, domain = None, None
                        if len(login_split) == 1:
                            username = login
                        elif len(login_split) == 2:
                            username, domain = login.split('@')

                        if domain is not None:
                            if domain not in settings.MASTER_DOMAINS:
                                sasl_logger.warning('Domain not in MASTER_DOMAINS', extra={
                                    'domain': domain,
                                    'result': 'Not Found'
                                })
                                return self.not_found()

                        if username is not None:
                            user = authenticate(username=username, password=password)
                            if user is not None:
                                if user.is_active:
                                    sasl_logger.info('Authentication OK, username: %s' % username)
                                    return self.success(self.passdb_payload(password))
                            sasl_logger.warning('Could not authenticate user', extra={
                                'username': username
                            })
                            return self.not_found()

            elif start_character == self.DICT_PROTOCOL_HOLONET_TEST_RESPONSE:
                return self.test({'content': line_payload})

        sasl_logger.warning('Could not parse payload: %s' % ', '.join(params), extra={
            'params': ', '.join(params)
        })
        return self.not_found()


class DovecotSASLHandler(BaseDovecotSASLHandler):

    handler = Handler()


class Command(SocketCommand):

    socket_location = 'sasl_authentication'
    handler_class = DovecotSASLHandler

    logger = sasl_logger


if __name__ == '__main__':
    command = Command()
    command.handle()
