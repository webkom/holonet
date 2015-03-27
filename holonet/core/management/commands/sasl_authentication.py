# -*- coding: utf8 -*-

import json

from django.conf import settings
from django.contrib.auth import authenticate
from . import SocketCommand, BaseDovecotSASLHandler


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
                except ValueError:
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
                                return self.not_found()

                        if username is not None:
                            user = authenticate(username=username, password=password)
                            if user is not None:
                                if user.is_active:
                                    return self.success(self.passdb_payload(password))
                            return self.not_found()

            elif start_character == self.DICT_PROTOCOL_HOLONET_TEST_RESPONSE:
                return self.test({'content': line_payload})

        return self.not_found()


class DovecotSASLHandler(BaseDovecotSASLHandler):

    handler = Handler()


class Command(SocketCommand):

    socket_location = 'sasl_authentication'
    handler_class = DovecotSASLHandler


if __name__ == '__main__':
    command = Command()
    command.handle()
