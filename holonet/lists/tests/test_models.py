from django.conf import settings
from django.db.utils import IntegrityError
from django.test import TestCase

from holonet.lists.models import MailingList, Recipient


class MappingModelTestCase(TestCase):
    fixtures = ['domains.yaml', 'mailing_lists.yaml', 'recipients.yaml']

    def test_recipients(self):
        mailing_list = MailingList.objects.get(pk=1)
        self.assertListEqual(mailing_list.recipients, ['testuser1@holonet.no',
                                                       'testuser2@holonet.no',
                                                       'testuser3@holonet.no'])

    def test_mapping_str(self):
        mapping = MailingList.objects.get(pk=1)
        self.assertEqual(str(mapping), mapping.prefix + '@' + settings.MASTER_DOMAIN)

    def test_duplicate_tags(self):
        mapping1 = MailingList.objects.get(pk=1)
        mapping2 = MailingList.objects.get(pk=2)

        mapping1.tag = 'duplicate'
        mapping2.tag = 'duplicate'

        mapping1.save()

        self.assertRaises(IntegrityError, mapping2.save)

    def test_deny_none_tag(self):
        mapping = MailingList.objects.get(pk=1)
        mapping.tag = None
        self.assertRaises(IntegrityError, mapping.save)


class RecipientModelTestCase(TestCase):

    fixtures = ['domains.yaml', 'mailing_lists.yaml', 'recipients.yaml']

    def test_duplicate_tags(self):
        recipient1 = Recipient.objects.get(pk=1)
        recipient2 = Recipient.objects.get(pk=2)

        recipient1.tag = 'duplicate'
        recipient2.tag = 'duplicate'

        recipient1.save()

        self.assertRaises(IntegrityError, recipient2.save)

    def test_allow_none_tag(self):
        recipient = Recipient.objects.get(pk=1)
        recipient.tag = None
        self.assertRaises(IntegrityError, recipient.save)

    def test_recipient_member_lists(self):
        recipient = Recipient.objects.get(pk=1)
        self.assertListEqual(recipient.lists, ['testlist1', 'testlist4'])

    def test_recipient_str(self):
        recipient = Recipient.objects.get(pk=1)
        self.assertEqual(recipient.address, str(recipient))
