# -*- coding: utf8 -*-

from django.core.management.base import BaseCommand
from optparse import make_option
import sys
import threading
import socketserver
import signal
import time

from django.conf import settings


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class PostfixAccessPolicyHandler(socketserver.BaseRequestHandler):
    # Protocol: http://www.postfix.org/SMTPD_POLICY_README.html
    # Access response codes: http://www.postfix.org/access.5.html

    def consider(self, params):
        """Consider a set of params sent by postfix and
           see if we want to hadle mail for the address"""

        if not 'recipient' in params:
            return {'action': 'REJECT No recipient listed'}

        recipient = params["recipient"]
        splitted = recipient.split('@')

        if len(splitted) < 2:
            return {'action': 'REJECT Address incomplete'}

        prefix, domain = splitted

        if domain in settings.MASTER_DOMAINS:

            if prefix == 'eirik':
                return {'action': 'DUNNO'}
            else:
                return {'action': 'REJECT Address does not exist'}

        else:
                return {'action': 'REJECT Domain is not handled by holonet'}

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
        make_option('--test-option', action='store_false', dest='use_test', default=False,
                    help='Does test things'),
    )
    help = "Start a daemon for verifying access with postfix smtp access policy deligation"
    args = '<server host> <port> (default localhost 10336'

    def handle(self, *args, **options):
        if args:
            host = args[0]
            port = args[1]
        else:
            host = "localhost"
            port = 13000
        server = ThreadedTCPServer((host, port), PostfixAccessPolicyHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        def handler(signum, frame):
            if signum == signal.SIGTERM:
                server.shutdown()
                sys.exit(0)
        signal.signal(signal.SIGTERM, handler)

        while True:
            time.sleep(5.0)


if __name__ == '__main__':
    command = Command()
    command.handle()
