# -*- coding: utf8 -*-

import email
import os

from django.test import TestCase
from django.core import mail
from django.conf import settings

from holonet.core.management.commands.mail_handler import Command as MailCommand


class MailHandlerCommandTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def setUp(self):
        file_path = '%s/email.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        self.message = email.message_from_file(email_file)
        self.command = MailCommand()

    def test_one_recipient(self):
        self.command.handle('testlist1@test.holonet.no', file=self.message)
        self.assertEqual(len(mail.outbox), 1)

    def test_system_alias_recipient(self):
        self.command.handle(settings.SYSTEM_ALIASES[0], file=self.message)
        result = mail.outbox[0]
        self.assertIn(settings.SERVER_EMAIL, result['args'])
        for admin in settings.ADMINS:
            self.assertIn(admin[1], result['args'])
