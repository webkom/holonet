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
    # Initialize variables
    sender = sender.lower()
    recipient = recipient.lower()
    domain = settings.MASTER_DOMAINS[0]

    # Check that the recipient is valid and exist in our catalog
    validate_recipient(recipient=recipient, sys_exit=True)

    try:
        # Spilt the recipient address into prefix an domain
        splitted_recipient = recipient.split('@')
        prefix, domain = splitted_recipient
    except ValueError:
        # We got no @, this happens when the server sends out a error message.
        if '@' not in recipient and recipient in settings.SYSTEM_ALIASES:
            prefix = recipient
        else:
            sys.exit(settings.EXITCODE_UNKNOWN_RECIPIENT)

    # Handle restricted mail. Send out new messages based on out lists.
    if prefix == settings.RESTRICTED_PREFIX:
        raise NotImplemented('Restricted mail is not ready')

    # Handle bounce
    if prefix == settings.SERVER_EMAIL.split('@')[0]:
        message = HolonetEmailMessage(msg, [], list_name=prefix)
        try:
            index_bounce_mail.delay(message)
            send_bounce_notification.delay(message)
        except OSError:
            pass
        return True

    # Lookup valid recipients
    try:
        recipients = MailingList.objects.get(prefix=prefix).recipients
    except MailingList.DoesNotExist:
        # Check SYSTEM_ALIASES, if ok, send to system admins.
        if prefix in settings.SYSTEM_ALIASES:
            recipients = [address[1] for address in settings.ADMINS]
        else:
            sys.exit(settings.EXITCODE_UNKNOWN_RECIPIENT)

    # Generate the final message
    message = HolonetEmailMessage(msg, recipients, list_name=prefix)

    # Check if spamassasin has marked the message as spam.
    spam_flag = message.get('X-Spam-Flag', False)
    if spam_flag == 'YES':
        try:
            index_spam.delay(message)
            send_spam_notification.delay(message)
        except OSError:
            pass
        return True

    # Check if the sender is blacklisted.
    if is_blacklisted(sender):
        try:
            index_blacklisted_mail.delay(message)
            send_blacklist_notification.delay(message)
        except OSError:
            pass
        return True

    # Sent the message!
    if not settings.TESTING:
        message.send()
    else:
        # Use holonet backend in testing, not locmem
        from holonet.backends.sendmail import EmailBackend
        backend = EmailBackend()
        backend.send_messages([message])
