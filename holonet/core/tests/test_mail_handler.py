# -*- coding: utf8 -*-

import os
import email
import math

from django.test import TestCase
from django.conf import settings
from django.core import mail

from holonet.core.handler import handle_mail
from holonet.mappings.models import MailingList, Recipient


class MailHandlerTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def setUp(self):
        file_path = '%s/email.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        self.message = email.message_from_file(email_file)

    def test_handle_email_unknown_prefix(self):
        with self.assertRaises(SystemExit) as cm:
            handle_mail(self.message, 'eirik@sylliaas.no', 'test@test.holonet.no')

        self.assertEqual(cm.exception.code, settings.EXITCODE_UNKNOWN_RECIPIENT)

    def test_handle_email_invalid_domain(self):
        with self.assertRaises(SystemExit) as cm:
            handle_mail(self.message, 'eirik@sylliaas.no', 'testlist1@holonetinvalid.no')

        self.assertEqual(cm.exception.code, settings.EXITCODE_UNKNOWN_DOMAIN)

    def test_valid_handler(self):
        mail_mapping = MailingList.objects.get(pk=1)
        for i in range(5, 300):
            mail_mapping.recipient_list.create(
                address='testlist%s@%s' % (i, settings.MASTER_DOMAINS[0]),
                tag=i
            )

        handle_mail(self.message, 'eirik@sylliaas.no', 'testlist1@test.holonet.no')

        recipient_count = mail_mapping.recipient_list.count()
        batches = math.ceil(recipient_count/settings.SENDMAIL_BATCH_LENGTH)

        self.assertEqual(len(mail.outbox), batches)

        handler_recipients = []
        for message in mail.outbox:
            args = message['args']
            handler_recipients += args[5:]

        self.assertListEqual(handler_recipients, mail_mapping.recipients)

    def test_spam_handling(self):
        file_path = '%s/email_spam.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        msg = email.message_from_file(email_file)
        self.assertEqual(handle_mail(msg, 'eirik@sylliaas.no', 'testlist1@test.holonet.no'), True)
