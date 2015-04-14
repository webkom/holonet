# -*- coding: utf8 -*-

import logging
from urllib.parse import urlparse

from django.conf import settings

from holonet.core.validation import validate_recipient

from . import BasePostfixPolicyServiceHandler, SocketCommand

incoming_logger = logging.getLogger('holonet.incoming_policy')


class Handler(object):
    """
    This service validates normal incoming mail.
    """
    def consider(self, params):
        recipient = 'UNKNOWN'
        if params:
            recipient = params.get('recipient', 'UNKNOWN')

        recipient_validation = validate_recipient(params=params)

        incoming_logger.info('Incomming email to %s, result: %s' %
                             (recipient, recipient_validation.get('action')))

        return recipient_validation


class PostfixPolicyServiceHandler(BasePostfixPolicyServiceHandler):
    handler = Handler()


class Command(SocketCommand):

    parser = urlparse(settings.INCOMING_SOCKET_LOCATION)
    host = parser.hostname
    port = parser.port

    logger = incoming_logger

    socket_location = (host, port)
    handler_class = PostfixPolicyServiceHandler
    tcp_stream = True

if __name__ == '__main__':
    command = Command()
    command.handle()
