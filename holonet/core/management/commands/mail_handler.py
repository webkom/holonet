# -*- coding: utf8 -*-

import email
import sys

from django.core.management.base import BaseCommand

from holonet.core.handler import handle_mail


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (

    )
    requires_model_validation = True
    help = "Processes a mail"
    args = '<sender> <recipients>'

    def handle(self, sender, *recipients, **options):
        msg = email.message_from_file(sys.stdin)
        for recipient in recipients:
            handle_mail(msg, sender, recipient)
