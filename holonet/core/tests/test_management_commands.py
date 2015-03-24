# -*- coding: utf8 -*-

import email
import json
import os

from django.conf import settings
from django.core import mail
from django.test import TestCase

from holonet.core.management.commands.mail_handler import Command as MailCommand
from holonet.core.management.commands.sasl_authentication import HolonetSASLHandler


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


class SASLHandlerCommandTestCase(TestCase):

    def setUp(self):
        self.handler = HolonetSASLHandler()

    def test_constants(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_HELLO, 'H')
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_LOOKUP, 'L')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_OK, 'O')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, 'N')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_FAIL, 'F')

    def test_success_string(self):
        payload = self.handler.userdb_payload()
        self.assertEqual('%s%s' % (self.handler.DICT_PROTOCOL_REPLY_OK, json.dumps(payload)),
                         self.handler.success(payload))

    def test_not_found_string(self):
        payload = self.handler.userdb_payload()
        self.assertEqual('%s%s' % (self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, json.dumps(payload)),
                         self.handler.not_found(payload))
