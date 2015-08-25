from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from holonet.status import manager


class TestViewSets(APITestCase):

    fixtures = ['users.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))

    def test_types(self):
        url = '/status/types/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_list(self):
        url = '/status/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_retrive(self):
        status_classes = manager.keys()
        for status_class in status_classes:
            class_instance = manager.get(status_class)()
            url = '/status/%s/' % class_instance.name
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_unknown_status(self):
        url = '/status/unknown_service/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
