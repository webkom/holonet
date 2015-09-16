from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ViewsTestCase(APITestCase):

    fixtures = ['users.yaml']

    def test_auth_browse(self):
        user = User.objects.get(username='holonet_admin')
        self.client.force_authenticate(user)
        response = self.client.get(reverse('api:browse'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_noauth_bowse(self):
        self.client.force_authenticate(None)
        response = self.client.get(reverse('api:browse'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
