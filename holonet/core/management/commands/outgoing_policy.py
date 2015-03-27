# -*- coding: utf8 -*-

from django.conf import settings

from . import BasePostfixPolicyServiceHandler, UnixCommand


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


class Command(UnixCommand):

    socket_location = settings.OUTGOING_SOCKET_LOCATION
    handler_class = PostfixPolicyServiceHandler


if __name__ == '__main__':
    command = Command()
    command.handle()
