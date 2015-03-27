# -*- coding: utf8 -*-

from urllib.parse import urlparse

from django.conf import settings

from . import BasePostfixPolicyServiceHandler, SocketCommand


class Handler(object):
    """
    This service validates submission
    """
    def consider(self, params):

        exit_options = {
            'accept': {'action': '%s ' % settings.ACCEPT_ACTION},
            'reject': {'action': '%s ' % settings.REJECT_ACTION},
        }

        sender = params.get('sender', None)
        sasl_username = params.get('sasl_username', None)

        def send_result(result):
            payload = exit_options.get(result, None)
            if payload is None:
                payload = exit_options.get('reject')

            return payload

        if sender and sasl_username:

            # Do a lookup
            return send_result('accept')

        return send_result('accept')


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
