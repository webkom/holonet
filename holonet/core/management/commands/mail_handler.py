# -*- coding: utf8 -*-

import email
import sys

from django.conf import settings
from django.core.management.base import BaseCommand

from holonet.core.handler import handle_mail


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    requires_model_validation = True
    help = "Processes a mail"
    args = '<sender> <recipients>'

    def handle(self, sender, *recipients, **options):
        if not settings.TESTING:
            msg = email.message_from_file(sys.stdin)
        else:
            # Used for testing
            msg = options['file']

        for recipient in recipients:
            handle_mail(msg, sender, recipient)

        # Handle calls with no sender, only a recipient.
        # The recipient list is then empty and the sender is the recipient.
        if sender and len(recipients) == 0:
            handle_mail(msg, settings.SERVER_EMAIL, sender)
