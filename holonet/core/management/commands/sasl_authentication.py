# -*- coding: utf8 -*-

import os
import socket
import sys

from django.core.management.base import BaseCommand

server_address = './sasl'


class Command(BaseCommand):

    help = "Test submission login"

    def handle(self, *args, **kwargs):

        try:
            os.unlink(server_address)
        except OSError:
            if os.path.exists(server_address):
                print('Socket exists.')
                sys.exit(1)

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(server_address)

        sock.listen(1)

        while True:
            connection, client_address = sock.accept()
            try:
                while True:
                    data = connection.recv(1024)
                    if data:

                        file = open('/tmp/submission', 'w')
                        file.write(data.decode())
                        file.close()

                    else:
                        break

            finally:
                connection.close()
