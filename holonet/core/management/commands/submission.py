# -*- coding: utf8 -*-

import email
import sys

from django.conf import settings
from django.core.management.base import BaseCommand

from holonet.core.message import HolonetEmailMessage
from holonet.core.tasks import call_task, index_spam, index_statistics


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    requires_model_validation = True
    help = "Processes a submission mail"
    args = '<sender> <recipients>'

    def send_mail(self, message, sender, recipients):
        # Initialize message
        message = HolonetEmailMessage(message, recipients)

        # Check if spamassasin has marked the message as spam.
        spam_flag = message.get('X-Spam-Flag', False)
        if spam_flag == 'YES':
            call_task(index_spam, message)
            sys.exit(0)

        call_task(index_statistics, sender=sender, list='submission', recipients=recipients)

        # Send the message!
        if not settings.TESTING:
            message.send()
        else:
            # Use holonet backend in testing, not locmem
            from holonet.backends.sendmail import EmailBackend
            backend = EmailBackend()
            backend.send_messages([message])

    def handle(self, sender, *recipients, **options):
        if not settings.TESTING:
            msg = email.message_from_file(sys.stdin)
        else:
            # Used for testing
            msg = options['file']

        if len(recipients) > 0:
            self.send_mail(msg, sender, recipients)

        # Handle calls with no sender, only a recipient.
        # The recipient list is then empty and the sender is the recipient.
        if sender and len(recipients) == 0:
            self.send_mail(msg, settings.SERVER_EMAIL, [sender])
