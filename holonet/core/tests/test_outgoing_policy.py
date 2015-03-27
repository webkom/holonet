# -*- coding: utf8 -*-

from django.conf import settings
from django.test import TestCase

from holonet.core.management.commands.outgoing_policy import Handler


class OutgoingPolicyServiceTestCase(TestCase):

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
            'sender': 'holonet@holonet.no'
        }

        result = self.handler.consider(payload)
        self.assertTrue(result['action'].startswith(settings.ACCEPT_ACTION))
