# -*- coding: utf8 -*-

import signal
import socketserver
import sys
import threading
import time
from urllib.parse import urlparse

from django.conf import settings
from django.core.management.base import BaseCommand

from holonet.core.validation import validate_recipient


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class HolonetAccessPolicyHandler(object):
    def consider(self, params):
        return validate_recipient(params=params)


class PostfixAccessPolicyHandler(socketserver.BaseRequestHandler, HolonetAccessPolicyHandler):
    # Protocol: http://www.postfix.org/SMTPD_POLICY_README.html
    # Access response codes: http://www.postfix.org/access.5.html

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
        response = self.consider(params)

        self.request.sendall(
            "\n".join(['='.join(item) for item in response.items()] + ['\n']).encode('utf-8')
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
        parser = urlparse(settings.POLICYSERVICE_URL)
        host = parser.hostname
        port = parser.port

        server = ThreadedTCPServer((host, port), PostfixAccessPolicyHandler)
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
