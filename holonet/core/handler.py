# -*- coding: utf8 -*-

import sys

from django.conf import settings

from holonet.core.tasks import (call_task, index_blacklisted_mail, index_bounce_mail, index_spam,
                                index_statistics)
from holonet.mappings.helpers import (clean_address, is_bounce, is_server_alias, lookup,
                                      split_address)
from holonet.restricted.helpers import is_restricted

from .blacklist import is_blacklisted
from .message import HolonetEmailMessage
from .validation import validate_recipient


def handle_mail(msg, sender, recipient):
    """
    Process mail. Lookup recipients and forward it using sendmail.
    """

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
        call_task(index_blacklisted_mail, message)
        return True

    # Check if spamassasin has marked the message as spam.
    spam_flag = message.get('X-Spam-Flag', False)
    if spam_flag == 'YES':
        call_task(index_spam, message)
        return True

    # Handle bounce
    if is_bounce(prefix):
        call_task(index_bounce_mail, message)
        return True

    # Exit with a exitcode if restricted mail don't have any recipients
    if is_restricted(prefix) and len(recipient) == 0:
        sys.exit(settings.EXITCODE_UNKNOWN_RECIPIENT)

    # Store statistics
    if not is_restricted(prefix) and not is_server_alias(prefix):
        call_task(index_statistics, sender=sender, list=prefix, recipients=recipients)

    # Send the message!
    if not settings.TESTING:
        message.send()
    else:
        # Use holonet backend in testing, not locmem
        from holonet.backends.sendmail import EmailBackend
        backend = EmailBackend()
        backend.send_messages([message])
