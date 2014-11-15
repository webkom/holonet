# -*- coding: utf8 -*-

from omnibus.api import publish
from omnibus.exceptions import OmnibusDataException, OmnibusPublisherException

from django.conf import settings
from django.utils.html import escape


def notify_spam(message):
    body_message = 'Holonet received a spam mail.'

    from_address = message.get('From')
    if from_address:
        body_message = escape('Mail from %s was marked as spam.' % (from_address, ))

    try:
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
    except OmnibusDataException:
        pass
    except OmnibusPublisherException:
        pass
