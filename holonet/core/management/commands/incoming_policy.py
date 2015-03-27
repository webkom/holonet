# -*- coding: utf8 -*-

from urllib.parse import urlparse

from django.conf import settings

from holonet.core.validation import validate_recipient

from . import BasePostfixPolicyServiceHandler, SocketCommand


class Handler(object):
    """
    This service validates normal incoming mail.
    """
    def consider(self, params):
        return validate_recipient(params=params)


class PostfixPolicyServiceHandler(BasePostfixPolicyServiceHandler):
    handler = Handler()


class Command(SocketCommand):

    parser = urlparse(settings.INCOMING_SOCKET_LOCATION)
    host = parser.hostname
    port = parser.port

    socket_location = (host, port)
    handler_class = PostfixPolicyServiceHandler
    tcp_stream = True

if __name__ == '__main__':
    command = Command()
    command.handle()
