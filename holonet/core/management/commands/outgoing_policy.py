# -*- coding: utf8 -*-

import logging
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import User

from holonet.lists.helpers import clean_address, lookup, split_address

from . import BasePostfixPolicyServiceHandler, SocketCommand

outgoing_logger = logging.getLogger('holonet.outgoing_policy')


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

        def send_result(result, log=None):
            payload = exit_options.get(result, None)
            if payload is None:
                payload = exit_options.get('reject')

            if log:
                outgoing_logger.info('%s, result: %s' % (log, payload.get('action')))

            return payload

        test = params.get('test', '0')
        if test == '1':
            return send_result('test', False)

        if sender and sasl_username:

            outgoing_logger.info('Got outgoing submission email from %s@%s' %
                                 (sender, sasl_username))

            sender = clean_address(sender)
            prefix, domain = split_address(sender)

            try:

                user = User.objects.get(username=sasl_username)
                user_email = user.email
                if user_email and domain in settings.MASTER_DOMAINS:
                    valid_user_lists = lookup(prefix)
                    if user_email in valid_user_lists:
                        return send_result('accept', 'User has a valid list')

            except User.DoesNotExist:
                pass

            return send_result('reject', 'User do not have a valid list')

        return send_result('accept', 'Could not do a successful lookup')


class PostfixPolicyServiceHandler(BasePostfixPolicyServiceHandler):

    handler = Handler()


class Command(SocketCommand):

    parser = urlparse(settings.OUTGOING_SOCKET_LOCATION)
    host = parser.hostname
    port = parser.port

    logger = outgoing_logger

    socket_location = (host, port)
    handler_class = PostfixPolicyServiceHandler
    tcp_stream = True


if __name__ == '__main__':
    command = Command()
    command.handle()
