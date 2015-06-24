# -*- coding: utf8 -*-

import email
import logging
import sys

from django.conf import settings
from django.core.management.base import BaseCommand

from holonet.core.message import HolonetEmailMessage

logger = logging.getLogger('holonet.submission')


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
            # TODO: Index spam message
            sys.exit(0)

        # Send the message!
        if not settings.TESTING:
            message.send()
        else:
            # Use holonet backend in testing, not locmem
            from holonet.backends.sendmail import EmailBackend
            backend = EmailBackend()
            backend.send_messages([message])

    def handle(self, sender, *recipients, **options):
        try:
            if not settings.TESTING:
                msg = email.message_from_binary_file(sys.stdin.buffer)
            else:
                # Used for testing
                msg = options['file']

            if len(recipients) > 0:
                logger.info(
                    'Received email from %s, forwarding it to %s' %
                    (sender, ', '.join(recipients)),
                    extra={
                        'sender': sender,
                        'recipients': ', '.join(recipients)
                        }
                )
                self.send_mail(msg, sender, recipients)

            # Handle calls with no sender, only a recipient.
            # The recipient list is then empty and the sender is the recipient.
            if sender and len(recipients) == 0:
                logger.info(
                    'Received email from %s, forwarding it to %s' %
                    (settings.SERVER_EMAIL, ', '.join([sender])),
                    extra={
                        'sender': settings.SERVER_EMAIL,
                        'recipients': sender
                        }
                )
                self.send_mail(msg, settings.SERVER_EMAIL, [sender])

        except Exception as e:
            logger.exception(e)
            sys.exit(1)
