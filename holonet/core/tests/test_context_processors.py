# -*- coding: utf8 -*-

from omnibus.authenticators import UserAuthenticator
from omnibus.settings import SERVER_PORT, SERVER_HOST, ENDPOINT_SCHEME, SERVER_BASE_URL
from omnibus.compat import split_domain_port

from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.test.utils import override_settings
from django.conf import settings

from holonet.core.context_processors import omnibus


class ContectProcessorTestCase(TestCase):
    fixtures = ['users.yaml']

    def setUp(self):
        self.factory = RequestFactory()

    def check_response(self, response, endpoint, user):
        self.assertEqual(response['OMNIBUS_ENDPOINT'], endpoint)
        if user.is_authenticated():
            auth_token = '{0}:{1}'.format(user.pk, UserAuthenticator.get_auth_token(user.pk))
            self.assertEqual(response['OMNIBUS_AUTH_TOKEN'], auth_token)
        else:
            self.assertEqual(response['OMNIBUS_AUTH_TOKEN'], '')

    def test_omnibus_context_processor_nouser_localhost(self):
        request = self.factory.request()
        request.user = AnonymousUser()
        request.get_host()
        request.META['HTTP_HOST'] = '127.0.0.1:8080'

        self.check_response(
            response=omnibus(request),
            endpoint='{0}://{1}:{2}{3}'.format(
                ENDPOINT_SCHEME,
                SERVER_HOST or split_domain_port(request.get_host())[0],
                SERVER_PORT,
                SERVER_BASE_URL
            ),
            user=AnonymousUser()
        )

    @override_settings(OMNIBUS_ENDPOINT_SCHEME='https')
    def test_omnibus_context_processor_nouser_localhost_https(self):
        request = self.factory.request()
        request.user = AnonymousUser()
        request.get_host()
        request.META['HTTP_HOST'] = 'localhost:8080'

        self.check_response(
            response=omnibus(request),
            endpoint='{0}://{1}:{2}{3}'.format(
                settings.OMNIBUS_ENDPOINT_SCHEME,
                SERVER_HOST or split_domain_port(request.get_host())[0],
                SERVER_PORT,
                SERVER_BASE_URL
            ),
            user=AnonymousUser()
        )

    def test_omnibus_context_processor_user_localhost(self):
        user = User.objects.first()
        request = self.factory.request()
        request.user = user
        request.get_host()
        request.META['HTTP_HOST'] = '127.0.0.1:8080'

        self.check_response(
            response=omnibus(request),
            endpoint='{0}://{1}:{2}{3}'.format(
                ENDPOINT_SCHEME,
                SERVER_HOST or split_domain_port(request.get_host())[0],
                SERVER_PORT,
                SERVER_BASE_URL
            ),
            user=user
        )

    @override_settings(OMNIBUS_ENDPOINT_SCHEME='https')
    def test_omnibus_context_processor_user_https(self):
        user = User.objects.first()
        request = self.factory.request()
        request.user = user
        request.get_host()
        request.META['HTTP_HOST'] = '192.168.0.1:8080'

        self.check_response(
            response=omnibus(request),
            endpoint='{0}://{1}:{2}{3}'.format(
                'https',
                SERVER_HOST or split_domain_port(request.get_host())[0],
                '443',
                SERVER_BASE_URL
            ),
            user=user
        )
