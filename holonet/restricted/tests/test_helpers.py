# -*- coding: utf8 -*-

import os
import email

from django.test import TestCase
from django.test.utils import override_settings

from holonet.restricted.helpers import get_payload_token, lookup
from holonet.restricted.models import RestrictedMapping


class TestHelpersTestCase(TestCase):

    fixtures = ['recipients.yaml', 'restricted_mappings.yaml']

    def setUp(self):
        file_path = '%s/multipart_attachment.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        self.message = email.message_from_file(email_file)
        self.token = '6375717d-9296-4db8-a0ec-40855cb94d79'

        file_path = '%s/short_token.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        self.short_token_message = email.message_from_file(email_file)

        file_path = '%s/multi_multipart_message.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        self.multi_message = email.message_from_file(email_file)

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_token_extractor(self):
        token = get_payload_token(self.message, remove_token=False)
        self.assertEquals(self.token, token)

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_short_token(self):
        token = get_payload_token(self.short_token_message, remove_token=False)
        self.assertIsNone(token)

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_token_remove(self):
        token = get_payload_token(self.message, remove_token=True)
        self.assertEquals(self.token, token)
        empty_token = get_payload_token(self.message, remove_token=True)
        self.assertIsNone(empty_token)

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_fwemail(self):
        token = get_payload_token(self.multi_message, remove_token=True)
        self.assertEquals(self.token, token)

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_lookup(self):
        mapping_recipients = RestrictedMapping.objects.get(token=self.token).recipients
        self.assertListEqual(mapping_recipients, lookup(self.message))

    @override_settings(RESTRICTED_TOKEN_PREFIX='holonet')
    def test_lookup_delete_token(self):
        mapping_recipients = RestrictedMapping.objects.get(token=self.token).recipients
        self.assertListEqual(mapping_recipients, lookup(self.message, mark_sent=True))
        self.assertEquals(RestrictedMapping.objects.get(token=self.token).is_used, True)
        self.assertIsNone(get_payload_token(self.message, True))
        self.assertListEqual(lookup(self.message, True), [])

    def test_empty_lookup(self):
        mapping_recipients = RestrictedMapping.objects.get(token=self.token)
        mapping_recipients.recipient_list.all().delete()
        self.assertListEqual(lookup(self.message, False), [])

    def test_toked_does_not_excist(self):
        RestrictedMapping.objects.get(token=self.token).delete()
        self.assertListEqual(lookup(self.message, False), [])
