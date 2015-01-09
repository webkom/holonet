# -*- coding: utf8 -*-

from omnibus.api import publish
from omnibus.exceptions import OmnibusDataException, OmnibusPublisherException

from django.conf import settings
from django.utils.html import escape


def send_notification(title, message, icon='fa fa-information', type='notification'):
    try:
        publish(
            settings.WEBSOCKET_CHANNEL,
            type,
            {
                'title': title,
                'message': message,
                'icon': icon
            },
            sender='holonet'
        )
    except OmnibusDataException:
        pass
    except OmnibusPublisherException:
        pass


def notify_spam(message):
    body_message = 'Holonet received a spam mail.'

    if message:
        from_address = message.get('From')
        if from_address:
            body_message = escape('Mail from %s was marked as spam.' % (from_address, ))

    send_notification('Spam Received', body_message, 'fa fa-trash')


def notify_blacklisted(message):
    body_message = 'Holonet received a blacklisted mail.'

    if message:
        from_address = message.get('From')
        if from_address:
            body_message = escape('Mail from %s was blacklisted.' % (from_address, ))

    send_notification('Blacklisted Mail Received', body_message, 'fa fa-warning')


def notify_bounce(message):
    body_message = 'Holonet received a bounce mail.'

    if message:
        from_address = message.get('From')
        if from_address:
            body_message = escape('Mail from %s was stores as bounce.' % (from_address, ))

    send_notification('Bounce Mail Received', body_message, 'fa fa-arrows-h')
