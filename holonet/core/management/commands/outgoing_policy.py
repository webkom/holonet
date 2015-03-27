# -*- coding: utf8 -*-

from urllib.parse import urlparse

from django.conf import settings

from . import BasePostfixPolicyServiceHandler, SocketCommand


class Handler(object):
    """
    This service validates submission
    """
    def consider(self, params):

        f = open('/tmp/submission', 'a')
        for key, value in params.items():
            f.write('%s: %s' % (key, value))
        f.close()

        return '%s  Forbidden Address' % (settings.REJECT_ACTION, )


class PostfixPolicyServiceHandler(BasePostfixPolicyServiceHandler):

    handler = Handler()


class Command(SocketCommand):

    parser = urlparse(settings.OUTGOING_SOCKET_LOCATION)
    host = parser.hostname
    port = parser.port

    socket_location = (host, port)
    handler_class = PostfixPolicyServiceHandler
    tcp_stream = True


if __name__ == '__main__':
    command = Command()
    command.handle()
