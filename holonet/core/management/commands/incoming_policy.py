# -*- coding: utf8 -*-

from django.conf import settings

from holonet.core.validation import validate_recipient

from . import BasePostfixPolicyServiceHandler, UnixCommand


class Handler(object):
    """
    This service validates normal incoming mail.
    """
    def consider(self, params):
        return validate_recipient(params=params)


class PostfixPolicyServiceHandler(BasePostfixPolicyServiceHandler):
    handler = Handler()


class Command(UnixCommand):

    socket_location = settings.INCOMING_SOCKET_LOCATION
    handler_class = PostfixPolicyServiceHandler

if __name__ == '__main__':
    command = Command()
    command.handle()
