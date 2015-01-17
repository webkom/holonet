# -*- coding: utf8 -*-

from django.test import TestCase
from django.conf import settings

from holonet.mappings.models import MailingList, Recipient


class ModelsTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def test_recipients(self):
        mailing_list = MailingList.objects.get(pk=1)
        self.assertListEqual(mailing_list.recipients, ['testuser1@holonet.no',
                                                       'testuser2@holonet.no',
                                                       'testuser3@holonet.no'])

    def test_mapping_str(self):
        mapping = MailingList.objects.get(pk=1)
        self.assertEqual(str(mapping), mapping.prefix + '@' + settings.MASTER_DOMAIN)

    def test_recipient_str(self):
        recipient = Recipient.objects.get(pk=1)
        self.assertEqual(recipient.address, str(recipient))
