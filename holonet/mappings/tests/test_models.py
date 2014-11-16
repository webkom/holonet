# -*- coding: utf8 -*-

from django.test import TestCase

from holonet.mappings.models import MailingList


class ModelsTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def test_recipients(self):
        mailing_list = MailingList.objects.get(pk=1)
        self.assertListEqual(mailing_list.recipients, ['testuser1@holonet.no',
                                                       'testuser2@holonet.no',
                                                       'testuser3@holonet.no'])
