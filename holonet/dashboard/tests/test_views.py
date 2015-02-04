# -*- coding: utf8 -*-

from django.contrib.auth.models import User
from django.test import Client, TestCase


class ViewsTestCase(TestCase):

    def setUp(self):
        username = 'testuser'
        password = 'pw'
        User.objects.create_user(username=username, password=password)

        self.auth_client = Client()
        self.auth_client.login(username=username, password=password)
        self.noauth_client = Client()

    def test_dashboard_view(self):
        result = self.auth_client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_dashboard_non_login(self):
        result = self.noauth_client.get('/')
        self.assertEqual(result.status_code, 302)
