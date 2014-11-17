# -*- coding: utf8 -*-

from django.test import TestCase

from holonet.core.blacklist import is_blacklisted


class ModelsTestCase(TestCase):
    fixtures = ['blacklist.yaml']

    def test_invalid_mail(self):
        self.assertFalse(is_blacklisted('invalidmail.com'))
        self.assertFalse(is_blacklisted('unknown@'))

    def test_valid_mail_no_blacklist(self):
        self.assertFalse(is_blacklisted('valid_mail@holonet.no'))

    def test_blacklisted_email(self):
        self.assertTrue(is_blacklisted('testblacklist1@abakus.no'))
        self.assertTrue(is_blacklisted('testblacklist2@holonet.no'))
        self.assertTrue(is_blacklisted('testblacklist3@holonet.no'))

    def test_blacklisted_domain(self):
        self.assertTrue(is_blacklisted('test_balcklist@blacklisted.no'))
        self.assertTrue(is_blacklisted('blacklisted.no'))
