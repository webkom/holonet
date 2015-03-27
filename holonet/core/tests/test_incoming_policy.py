# -*- coding: utf8 -*-

from django.conf import settings
from django.test import TestCase

from holonet.core.management.commands.incoming_policy import Handler


class IncomingPolicyServiceTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'recipients.yaml']

    def setUp(self):
        self.policy_service = Handler()

    def test_consider_no_recipient(self):
        result = self.policy_service.consider({})
        action = result['action']
        self.assertTrue(action.startswith(settings.REJECT_ACTION))

    def test_consider_invalid_recipient(self):
        result = self.policy_service.consider({'recipient': 'test1'})
        action = result['action']
        self.assertTrue(action.startswith(settings.REJECT_ACTION))

    def test_consider_invalid_master_domain(self):
        result = self.policy_service.consider({'recipient': 'test1@test.invalid.no'})
        action = result['action']
        self.assertTrue(action.startswith(settings.REJECT_ACTION))

    def test_consider_unmanaged_recpient(self):
        result = self.policy_service.consider(
            {
                'recipient': 'test@%s' % settings.MASTER_DOMAIN
            })

        action = result['action']
        self.assertTrue(action.startswith(settings.REJECT_ACTION))

    def test_consider_managed_recipient(self):
        result = self.policy_service.consider(
            {
                'recipient': 'testlist1@%s' % settings.MASTER_DOMAIN
            })

        action = result['action']
        self.assertTrue(action.startswith(settings.ACCEPT_ACTION))
