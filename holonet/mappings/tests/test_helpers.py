# -*- coding: utf8 -*-

from django.test import TestCase
from django.conf import settings

from holonet.mappings.helpers import is_prefix_valid


class HelperTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def test_is_prefix_valid(self):
        self.assertTrue(is_prefix_valid('testlist1'))
        self.assertTrue(is_prefix_valid('testlist2'))
        self.assertFalse(is_prefix_valid('testlist3'))
        self.assertFalse(is_prefix_valid('testlist4'))
        self.assertTrue(is_prefix_valid(settings.RESTRICTED_PREFIX))
        self.assertTrue(is_prefix_valid(settings.SERVER_EMAIL.split('@')[0]))
