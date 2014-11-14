# -*- coding: utf8 -*-

from django.test import TestCase
from django.conf import settings

from holonet.core.management.commands.policy_service import HolonetAccessPolicyHandler


class PolicyServiceTestCase(TestCase):
    fixtures = ['mailing_lists.yaml', 'members.yaml']

    def setUp(self):
        self.policy_service = HolonetAccessPolicyHandler()

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
                'recipient': 'test@%s' % settings.MASTER_DOMAINS[0]
            })

        action = result['action']
        self.assertTrue(action.startswith(settings.REJECT_ACTION))

    def test_consider_managed_recipient(self):
        result = self.policy_service.consider(
            {
                'recipient': 'testlist1@%s' % settings.MASTER_DOMAINS[0]
            })

        action = result['action']
        self.assertTrue(action.startswith(settings.ACCEPT_ACTION))
