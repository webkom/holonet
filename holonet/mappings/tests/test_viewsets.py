# -*- coding: utf8 -*-

from django.conf import settings
from rest_framework.test import APITestCase

from holonet.core.models import HolonetUser as User
from holonet.mappings.helpers import lookup
from holonet.mappings.models import MailingList


class ReverseLookupTestCase(APITestCase):

    fixtures = ['users.yaml', 'mailing_lists.yaml', 'recipients.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))
        self.endpoint = '/api/lookup/lookup/'

    def test_reverse_lookup(self):
        stored_recipients = MailingList.objects.get(prefix='testlist1').recipients

        data = {
            'email': 'testlist1'
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEqual(len(response.data), len(stored_recipients))

        data = {
            'email': 'testlist1@%s' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEqual(len(response.data), len(stored_recipients))

        data = {
            'email': 'testlist1@%s@random' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEquals(len(response.data), len(lookup('testlist1')))

    def test_no_email(self):
        response = self.client.post(self.endpoint, format='json')

        self.assertListEqual(response.data, [])

    def test_unsupported_domain(self):
        data = {
            'email': 'testlist1@test.notsupported.no'
        }

        response = self.client.post(self.endpoint, data=data,  format='json')
        print(response.data)

        self.assertListEqual(response.data, [])

    def test_system_alias(self):
        data = {
            'email': '%s@%s' % (settings.SYSTEM_ALIASES[0], settings.MASTER_DOMAIN)
        }

        response = self.client.post(self.endpoint, data=data, format='json')

        self.assertEqual(len(response.data), len(settings.ADMINS))

    def test_no_mailinglist(self):
        data = {
            'email': 'unknown@%s' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data, format='json')

        self.assertListEqual(response.data, [])
