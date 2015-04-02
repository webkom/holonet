# -*- coding: utf8 -*-

from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import User

from holonet.mappings.helpers import clean_address, lookup, split_address

from . import BasePostfixPolicyServiceHandler, SocketCommand


class Handler(object):
    """
    This service validates submission
    """

    TEST_RESPONSE = 'TestOK'

    def consider(self, params):

        exit_options = {
            'accept': {'action': '%s ' % settings.ACCEPT_ACTION},
            'reject': {'action': '%s ' % settings.REJECT_ACTION},
            'test': {'action': '%s ' % self.TEST_RESPONSE},
        }

        sender = params.get('sender', None)
        sasl_username = params.get('sasl_username', None)

        def send_result(result):
            payload = exit_options.get(result, None)
            if payload is None:
                payload = exit_options.get('reject')

            return payload

        test = params.get('test', '0')
        if test == '1':
            return send_result('test')

        if sender and sasl_username:

            sender = clean_address(sender)
            prefix, domain = split_address(sender)

            try:

                user = User.objects.get(username=sasl_username)
                user_email = user.email
                if user_email and domain in settings.MASTER_DOMAINS:
                    valid_user_lists = lookup(prefix)
                    if user_email in valid_user_lists:
                        return send_result('accept')

            except User.DoesNotExist:
                pass

            return send_result('reject')

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
