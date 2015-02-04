# -*- coding: utf8 -*-

from django.conf import settings

from holonet.core.tasks import (index_blacklisted_mail, index_bounce_mail, index_spam,
                                send_blacklist_notification, send_bounce_notification,
                                send_spam_notification)
from holonet.mappings.helpers import clean_address, is_bounce, lookup, split_address

from .blacklist import is_blacklisted
from .message import HolonetEmailMessage
from .validation import validate_recipient


def handle_mail(msg, sender, recipient):
    # Initialize variables
    sender = clean_address(sender)
    recipient = clean_address(recipient)

    # Check that the recipient is valid and is handled by this server
    validate_recipient(recipient=recipient, sys_exit=True)

    # This prefix and domain is managed by this system.
    prefix, domain = split_address(recipient)

    # Lookup valid recipients
    recipients = lookup(prefix, msg, mark_restricted_as_used=True)

    # Generate the final message
    message = HolonetEmailMessage(msg, recipients, list_name=prefix)

    # Check if the sender is blacklisted.
    if is_blacklisted(sender):
        index_blacklisted_mail.delay(message)
        send_blacklist_notification.delay(message)
        return True

    # Check if spamassasin has marked the message as spam.
    spam_flag = message.get('X-Spam-Flag', False)
    if spam_flag == 'YES':
        index_spam.delay(message)
        send_spam_notification.delay(message)
        return True

    # Handle bounce
    if is_bounce(prefix):
        index_bounce_mail.delay(message)
        send_bounce_notification.delay(message)
        return True

    # Send the message!
    if not settings.TESTING:
        message.send()
    else:
        # Use holonet backend in testing, not locmem
        from holonet.backends.sendmail import EmailBackend
        backend = EmailBackend()
        backend.send_messages([message])
