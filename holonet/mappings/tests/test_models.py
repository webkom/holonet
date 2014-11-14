# -*- coding: utf8 -*-

from django.test import TestCase
from django.db.utils import IntegrityError

from holonet.mappings.models import MailingList


class ModelsTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'members.yaml']

    def test_recipients(self):
        mailing_list = MailingList.objects.get(pk=1)
        self.assertListEqual(mailing_list.recipients, ['testuser1@holonet.no',
                                                       'testuser2@holonet.no',
                                                       'testuser3@holonet.no'])

    def test_unique_members(self):
        mailing_list = MailingList.objects.get(pk=1)
        self.assertRaises(IntegrityError, mailing_list.members.create,
                          address='testuser1@holonet.no')
