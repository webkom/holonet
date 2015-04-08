# -*- coding: utf8 -*-

# -*- coding: utf8 -*-

import os
import signal
import socketserver
import sys
import threading
import time

from django.core.management.base import BaseCommand


class ThreadedUNIXStreamServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    pass


class ThreadedTCPStreamServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class BaseDovecotSASLHandler(socketserver.BaseRequestHandler):
    # Protocol: /src/lib-dict/dict-client.h

    handler = None

    def handle(self):

        packet = self.request.recv(1024)
        raw_data = packet.decode()
        params = raw_data.split('\n')

        response = self.handler.consider(params)

        self.request.sendall(
            (response + "\n").encode('utf-8')
        )


class BasePostfixPolicyServiceHandler(socketserver.BaseRequestHandler):
    # Protocol: http://www.postfix.org/SMTPD_POLICY_README.html
    # Access response codes: http://www.postfix.org/access.5.html

    handler = None

    def handle(self):
        """
        Pack and unpack the dicts used by consider to work with the
        postfix access policy checking protocol
        """
        # self.request is the TCP socket connected to the client
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

        params = dict([line.split("=", 1) for line in data])
        response = self.handler.consider(params)

        self.request.sendall(
            "\n".join(['='.join(item) for item in response.items()] + ['\n']).encode('utf-8')
        )


class SocketCommand(BaseCommand):

    socket_location = 'socket'
    handler_class = None
    tcp_stream = False

    logger = None

    option_list = BaseCommand.option_list + (

    )
    help = "Start a daemon for a unix socket"
    args = 'None'

    def __init__(self):
        super(SocketCommand, self).__init__()
        if not self.tcp_stream:
            self.server = ThreadedUNIXStreamServer(self.socket_location, self.handler_class)
        else:
            self.server = ThreadedTCPStreamServer(self.socket_location, self.handler_class)

    def _handle_sigterm(self, signum, frame):
        self.close()
        sys.exit(0)

    def _handle_sigusr1(self, signum, frame):
        self._handle_sigterm(signum, frame)

    def close(self):
        self.server.server_close()
        if not self.tcp_stream:
            if os.path.exists(self.socket_location):
                os.remove(self.socket_location)

    def handle(self, *args, **options):
        try:
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

        except Exception as e:
            self.logger.exception(e)
            sys.exit(1)
