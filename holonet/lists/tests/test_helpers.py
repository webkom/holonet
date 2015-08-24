from django.conf import settings
from django.test import TestCase

from holonet.lists.helpers import is_prefix_valid


class HelperTestCase(TestCase):
    fixtures = ['domains.yaml', 'mailing_lists.yaml', 'recipients.yaml']

    def test_is_prefix_valid(self):
        self.assertTrue(is_prefix_valid('testlist1'))
        self.assertTrue(is_prefix_valid('testlist2'))
        self.assertFalse(is_prefix_valid('testlist3'))
        self.assertTrue(is_prefix_valid('testlist4'))
        self.assertFalse(is_prefix_valid('testlist5'))
        self.assertTrue(is_prefix_valid(settings.RESTRICTED_PREFIX))
        self.assertTrue(is_prefix_valid(settings.SERVER_EMAIL.split('@')[0]))
