# -*- coding: utf8 -*-

import signal
import socketserver
import sys
import threading
import time

from django.core.management.base import BaseCommand

server_address = '.sasl'


class ThreadedUNIXStreamServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    pass


class HolonetSASLHandler(object):
    def consider(self, params):
        for line in params:
            if line.startswith('H'):
                pass
            elif line.startswith('L'):
                query = line[1:]
                namespace, query_type, arg = query.split('/')

                if namespace == 'shared':
                    if query_type == 'passdb':
                        return 'O{"password": "$1$JrTuEHAY$gZA1y4ElkLHtnsrWNHT/e.", "userdb_home"' \
                               ': "/home/username/", "userdb_uid": 1000, "userdb_gid": 1000}'

                    elif query_type == 'userdb':
                        return 'O{"home": "/home/username/", "uid": 1000, "gid": 1000}'


class DovecotSASLHandler(socketserver.BaseRequestHandler, HolonetSASLHandler):
    # Protocol: /src/lib-dict/dict-client.h

    def handle(self):
        data_list = []
        packet = self.request.recv(1024).decode('utf-8').split("\n")

        while ''.join(packet).strip():
            data_list.extend(packet)
            if data_list and not data_list[-1]:
                break
            packet = self.request.recv(1024).decode('utf-8').split("\n")

        data = filter(lambda line: len(line), data_list)
        if not data:
            return

        response = self.consider(data)

        self.request.sendall(
            (response + "\n").encode('utf-8')
        )


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    help = "Start a daemon for verifying access with postfix smtp access policy deligation"
    args = 'None'

    def _handle_sigterm(self, signum, frame):
        sys.exit(0)

    def _handle_sigusr1(self, signum, frame):
        self._handle_sigterm(signum, frame)

    def handle(self, *args, **options):

        server = ThreadedUNIXStreamServer(server_address, DovecotSASLHandler)
        server_thread = threading.Thread(target=server.serve_forever)
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
