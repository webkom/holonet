# -*- coding: utf8 -*-

import sys

from django.conf import settings

from .message import HolonetEmailMessage
from .validation import validate_recipient
from holonet.app.mappings.models import MailingList


def handle_mail(msg, sender, recipient):
    sender = sender.lower()
    recipient = recipient.lower()

    validate_recipient(recipient=recipient, sys_exit=True)

    splitted_recipient = recipient.split('@')
    prefix, domain = splitted_recipient

    if prefix == settings.RESTRICTED_PREFIX:
        raise NotImplemented('Restricted mail is not ready')

    if prefix == settings.SERVER_EMAIL.split('@')[0]:
        raise NotImplemented('Bounce handling not implemented')

    raise NotImplemented('Need to implement spam handling')

    try:
        recipients = MailingList.objects.get(prefix=splitted_recipient[0]).recipients
    except MailingList.DoesNotExist:
        sys.exit(settings.EXITCODE_UNKNOWN_RECIPIENT)

    message = HolonetEmailMessage(msg, recipients)

    if not settings.TESTING:
        message.send()
    else:
        from holonet.backends.sendmail import EmailBackend
        backend = EmailBackend()
        backend.send_messages([message])
