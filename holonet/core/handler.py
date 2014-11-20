# -*- coding: utf8 -*-

import sys

from django.conf import settings

from .blacklist import is_blacklisted
from .message import HolonetEmailMessage
from .validation import validate_recipient
from holonet.core.tasks import index_spam, send_spam_notification, index_blacklisted_mail, \
    send_blacklist_notification, index_bounce_mail, send_bounce_notification
from holonet.mappings.models import MailingList


def handle_mail(msg, sender, recipient):
    sender = sender.lower()
    recipient = recipient.lower()

    validate_recipient(recipient=recipient, sys_exit=True)

    splitted_recipient = recipient.split('@')
    prefix, domain = splitted_recipient

    if prefix == settings.RESTRICTED_PREFIX:
        raise NotImplemented('Restricted mail is not ready')

    if prefix == settings.SERVER_EMAIL.split('@')[0]:
        message = HolonetEmailMessage(msg, [], list_name=prefix)
        try:
            index_bounce_mail.delay(message)
            send_bounce_notification.delay(message)
        except OSError:
            pass
        return True

    try:
        recipients = MailingList.objects.get(prefix=prefix).recipients
    except MailingList.DoesNotExist:
        sys.exit(settings.EXITCODE_UNKNOWN_RECIPIENT)

    message = HolonetEmailMessage(msg, recipients, list_name=prefix)

    spam_flag = message.get('X-Spam-Flag', False)
    if spam_flag == 'YES':
        try:
            index_spam.delay(message)
            send_spam_notification.delay(message)
        except OSError:
            pass
        return True

    if is_blacklisted(sender):
        try:
            index_blacklisted_mail.delay(message)
            send_blacklist_notification.delay(message)
        except OSError:
            pass
        return True

    if not settings.TESTING:
        message.send()
    else:
        # Use holonet backend in testing, not locmem
        from holonet.backends.sendmail import EmailBackend
        backend = EmailBackend()
        backend.send_messages([message])
