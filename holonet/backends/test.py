# -*- coding: utf8 -*-

from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.test import TestCase

from .sendmail import EmailBackend


class TestEmailBackend(TestCase):
    def setUp(self):
        self.email_backend = EmailBackend()

    def test_email_backend(self):
        message = EmailMessage()
        message.to = ['test1@holonet.no']
        message.from_email = 'test2@holonet.no'
        message.subject = 'Test Subject'

        self.email_backend.send_messages([message])
        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(', '.join(message.to), mail.outbox[0]['message']['To'])
        self.assertEqual(message.from_email, mail.outbox[0]['message']['From'])
        self.assertEqual(message.subject, mail.outbox[0]['message']['Subject'])

        expected_args = [settings.SENDMAIL_EXECUTABLE, '-G', '-i', '-f', settings.SERVER_EMAIL]

        self.assertEqual(mail.outbox[0]['args'], expected_args + message.to)
