import email
import logging
import sys

from django.conf import settings
from django.core.management.base import BaseCommand

from holonet.core.handler import handle_mail

logger = logging.getLogger('holonet.mail_handler')


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    requires_model_validation = True
    help = "Processes a mail"
    args = '<sender> <recipients>'

    def handle(self, sender, *recipients, **options):
        try:
            if not settings.TESTING:
                msg = email.message_from_binary_file(sys.stdin.buffer)
            else:
                # Used for testing
                msg = options['file']

            for recipient in recipients:
                logger.info('Received email from %s, forwarding it to %s' %
                            (sender, recipient))
                handle_mail(msg, sender, recipient)

            # Handle calls with no sender, only a recipient.
            # The recipient list is then empty and the sender is the recipient.
            if sender and len(recipients) == 0:
                logger.info('Received email from %s, forwarding it to %s' %
                            (settings.SERVER_EMAIL, sender))
                handle_mail(msg, settings.SERVER_EMAIL, sender)
        except Exception as e:
            logger.exception(e)
            sys.exit(1)
