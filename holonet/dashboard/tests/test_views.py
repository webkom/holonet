# -*- coding: utf8 -*-

from django.contrib.auth.models import User
from django.test import Client, TestCase


class ViewsTestCase(TestCase):

    def setUp(self):
        username = 'testuser'
        password = 'pw'
        self.user = User.objects.create_user(username=username, password=password)

        self.auth_client = Client()
        self.auth_client.login(username=username, password=password)
        self.noauth_client = Client()

    def test_dashboard_view(self):
        self.user.is_staff = True
        self.user.save()
        result = self.auth_client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_dashboard_not_staff(self):
        self.user.is_staff = False
        self.user.save()
        result = self.auth_client.get('/', follow=True)
        self.assertEqual(result.wsgi_request.path, '/profile/')

    def test_dashboard_non_login(self):
        result = self.noauth_client.get('/')
        self.assertEqual(result.status_code, 302)

    def test_profile_view(self):
        result = self.auth_client.get('/profile/')
        self.assertEqual(result.status_code, 200)

    def test_profile_non_login(self):
        result = self.noauth_client.get('/profile/')
        self.assertEqual(result.status_code, 302)
