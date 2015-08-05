from django.test import TestCase
from rest_framework.test import APIRequestFactory

from holonet.api.backend import TokenAuthenticationBackend
from holonet.api.models import Token


class BackendTestCase(TestCase):
    fixtures = ['applications.yaml', 'tokens.yaml']

    def setUp(self):
        self.backend = TokenAuthenticationBackend()
        self.factory = APIRequestFactory()

    def test_valid_token(self):
        token = Token.objects.first()
        request = self.factory.get('/', HTTP_AUTHORIZATION=token.token)
        self.assertEquals(self.backend.authenticate(request), (token.application, request))

    def test_unknown_token(self):
        request = self.factory.get('/', HTTP_AUTHORIZATION='unknown')
        self.assertEquals(self.backend.authenticate(request), None)

    def test_none_token(self):
        request = self.factory.get('/')
        self.assertEquals(self.backend.authenticate(request), None)
