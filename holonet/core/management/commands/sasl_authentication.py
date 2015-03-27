# -*- coding: utf8 -*-

import json
import os
import signal
import socketserver
import sys
import threading
import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate


class ThreadedUNIXStreamServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    pass


class HolonetSASLHandler(object):

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


class DovecotSASLHandler(socketserver.BaseRequestHandler, HolonetSASLHandler):
    # Protocol: /src/lib-dict/dict-client.h

    def handle(self):

        packet = self.request.recv(1024)
        raw_data = packet.decode()
        params = raw_data.split('\n')

        response = self.consider(params)

        self.request.sendall(
            (response + "\n").encode('utf-8')
        )


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    help = "Start a daemon for verifying access for Dovecot sasl dict."
    args = 'None'

    def __init__(self):
        super(Command, self).__init__()
        self.server = ThreadedUNIXStreamServer(settings.SASL_SOCKET_LOCATION, DovecotSASLHandler)

    def _handle_sigterm(self, signum, frame):
        self.close()
        sys.exit(0)

    def _handle_sigusr1(self, signum, frame):
        self._handle_sigterm(signum, frame)

    def close(self):
        self.server.server_close()
        if os.path.exists(settings.SASL_SOCKET_LOCATION):
            os.remove(settings.SASL_SOCKET_LOCATION)

    def handle(self, *args, **options):

        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        # Gracefully exit on sigterm.
        signal.signal(signal.SIGTERM, self._handle_sigterm)

        # A SIGUSR1 signals an exit with an autorestart
        signal.signal(signal.SIGUSR1, self._handle_sigusr1)

        # Handle Keyboard Interrupt
        signal.signal(signal.SIGINT, self._handle_sigterm)

        while True:
            time.sleep(5.0)


if __name__ == '__main__':
    command = Command()
    command.handle()
    command.close()
