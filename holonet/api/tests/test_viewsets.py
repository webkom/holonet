from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from holonet.domains.models import Domain


class ViewSetTestCase(APITestCase):

    fixtures = ['users.yaml', 'domains.yaml']

    def setUp(self):

        self.client.force_authenticate(User.objects.get(pk=1))

    def test_information(self):

        url = '/information/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        self.assertListEqual(data.get('domains', []), Domain.list_domains())
        self.assertEqual(data.get('restricted_endpoint'), '%s@%s' % (settings.RESTRICTED_PREFIX,
                                                                     settings.MASTER_DOMAIN))
        self.assertEqual(data.get('sender_whitelist'), settings.SENDER_WHITELIST_ENABLED)
        self.assertEqual(data.get('domain_whitelist'), settings.DOMAIN_WHITELIST_ENABLED)
        self.assertEqual(data.get('system_owner'), settings.SYSTEM_OWNER)
        self.assertEqual(data.get('server_email'), settings.SERVER_EMAIL)
        self.assertEqual(data.get('system_aliases'), settings.SYSTEM_ALIASES)
        self.assertEqual(data.get('admins'), settings.ADMINS)

    def test_tasks(self):

        url = '/tasks/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        self.assertIsNotNone(data.get('regular'))
        self.assertIsNotNone(data.get('periodic'))
