# -*- coding: utf8 -*-

from django.conf import settings
from django.test import TestCase

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

    def test_duplicate_tags(self):
        mapping1 = MailingList.objects.get(pk=1)
        mapping2 = MailingList.objects.get(pk=2)

        mapping1.tag = '1'
        mapping2.tag = '1'

        mapping1.save()
        mapping1.save()

        self.assertRaises(ValueError, mapping2.save)

        mapping2.tag = ''
        self.assertIsNone(mapping2.save())

        mapping1.tag = ''
        self.assertIsNone(mapping1.save())

    def test_recipient_member_lists(self):
        recipient = Recipient.objects.get(pk=1)
        self.assertListEqual(recipient.lists, ['testlist1', 'testlist4'])
