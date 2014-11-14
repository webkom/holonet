# -*- coding: utf8 -*-

from omnibus.api import publish

from django.conf import settings


def notify_spam(message):
    body_message = 'Holonet received a spam mail.'

    from_address = message.get('From')
    if from_address:
        body_message = 'Mail from {sender} was marked as spam.'.format(sender=from_address)

    publish(
        settings.WEBSOCKET_CHANNEL,
        'notification',
        {
            'title': 'Spam Received',
            'message': body_message,
            'icon': 'fa fa-trash'
        },
        sender='holonet'
    )
