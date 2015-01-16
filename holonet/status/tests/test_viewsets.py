# -*- coding: utf8 -*-

from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from django.conf import settings
from django.utils.module_loading import import_string


class TestViewSets(APITestCase):

    fixtures = ['users.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))

    def test_types(self):
        url = '/api/status/types/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_list(self):
        url = '/api/status/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_retrive(self):
        status_classes = settings.STATUS_CLASSES
        for status_class in status_classes:
            class_instance = import_string(status_class)()
            url = '/api/status/%s/' % class_instance.name
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_unknown_status(self):
        url = '/api/status/unknown_service/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
