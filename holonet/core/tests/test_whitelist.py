# -*- coding: utf8 -*-

from django.test import TestCase
from django.test.utils import override_settings

from holonet.core.list_access import is_not_whitelisted


class WhitelistTestCase(TestCase):

    fixtures = ['whitelist.yaml']

    @override_settings(SENDER_WHITELIST_ENABLED=False, DOMAIN_WHITELIST_ENABLED=False)
    def test_whitelist_disabled(self):
        self.assertFalse(is_not_whitelisted('testwhitelist2@holonet.no'))
        self.assertFalse(is_not_whitelisted('test@whitelisted.no'))
        self.assertFalse(is_not_whitelisted('test@abakus.no'))

    @override_settings(SENDER_WHITELIST_ENABLED=False, DOMAIN_WHITELIST_ENABLED=True)
    def test_domain_whitelist(self):
        self.assertTrue(is_not_whitelisted('testwhitelist2@holonet.no'))
        self.assertFalse(is_not_whitelisted('test@whitelisted.no'))
        self.assertTrue(is_not_whitelisted('test@abakus.no'))

    @override_settings(SENDER_WHITELIST_ENABLED=True, DOMAIN_WHITELIST_ENABLED=True)
    def test_sender_domain_whitelist(self):
        self.assertFalse(is_not_whitelisted('testwhitelist2@holonet.no'))
        self.assertFalse(is_not_whitelisted('test@whitelisted.no'))
        self.assertTrue(is_not_whitelisted('test@abakus.no'))

    @override_settings(SENDER_WHITELIST_ENABLED=True, DOMAIN_WHITELIST_ENABLED=False)
    def test_sender_whitelist(self):
        self.assertFalse(is_not_whitelisted('testwhitelist2@holonet.no'))
        self.assertTrue(is_not_whitelisted('test@whitelisted.no'))
        self.assertTrue(is_not_whitelisted('test@abakus.no'))
