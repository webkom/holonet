# -*- coding: utf8 -*-

import email
import os

from django.core import mail
from django.test import TestCase, override_settings

from holonet.backends.sendmail import EmailBackend
from holonet.core.message import HolonetEmailMessage


class HolonetMessageTestCase(TestCase):

    def setUp(self):
        file_path = '%s/email.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        raw_message = email.message_from_file(email_file)

        self.message = HolonetEmailMessage(raw_message, ['holonet@holonet.no'])

    def test_values(self):
        self.assertIsInstance(self.message.values(), list)

    @override_settings(EMAIL_BACKEND='holonet.backends.sendmail.EmailBackend')
    def test_get_connection(self):
        self.assertIsInstance(self.message.get_connection(), EmailBackend)

    def test_send(self):
        self.message.send()
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0], self.message)

        self.message.list_recipients = []
        self.assertEqual(self.message.send(), 0)

    def test_as_bytes(self):
        result = self.message.as_bytes()
        self.assertIsInstance(result, bytes)
