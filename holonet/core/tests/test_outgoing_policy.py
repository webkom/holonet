# -*- coding: utf8 -*-

from django.conf import settings
from django.test import TestCase

from holonet.core.management.commands.outgoing_policy import Handler


class OutgoingPolicyServiceTestCase(TestCase):

    fixtures = ['users.yaml', 'domains.yaml', 'recipients.yaml', 'mailing_lists.yaml']

    def setUp(self):
        self.handler = Handler()

    def test_invalid_payload(self):

        payload = {
            'recipient': 'test@holonet.no'
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(settings.ACCEPT_ACTION))

    def test_valid_payload(self):

        payload = {
            'sasl_username': 'holonet',
            'sender': 'holonet@holonet.no',
            'test': '1'
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(Handler.TEST_RESPONSE))

    def test_invalid_sender_domain(self):

        payload = {
            'sasl_username': 'holonet',
            'sender': 'test@holonet.no'
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(settings.REJECT_ACTION))

    def test_valid_list_lookup(self):

        payload = {
            'sasl_username': 'testuser1',
            'sender': 'testlist1@%s' % settings.MASTER_DOMAIN
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(settings.ACCEPT_ACTION))

    def test_invalid_list_lookup(self):

        payload = {
            'sasl_username': 'testuser1',
            'sender': 'testlist3@%s' % settings.MASTER_DOMAIN
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(settings.REJECT_ACTION))
