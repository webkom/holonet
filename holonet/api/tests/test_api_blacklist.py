# -*- coding: utf8 -*-

from django.test import Client, TestCase

from holonet.api.models import Token
from holonet.core.serializers import DomainBlacklistSerializer, SenderBlacklistSerializer
from holonet.core.models import DomainBlacklist, SenderBlacklist


class BlacklistAPITestCase(TestCase):
    fixtures = ['blacklist.yaml', 'applications.yaml', 'tokens.yaml']

    def setUp(self):

        self.auth_client = Client(HTTP_X_TOKEN=Token.objects.first().token)
        self.noauth_client = Client()

    def test_list_domain_blacklist_no_auth(self):
        result = self.noauth_client.get('/api/domain-blacklist/')
        self.assertEquals(result.status_code, 403)

    def test_list_domain_blacklist_auth(self):
        result = self.auth_client.get('/api/domain-blacklist/')
        self.assertEquals(result.status_code, 200)

        serialized = DomainBlacklistSerializer(DomainBlacklist.objects.all(), many=True)
        self.assertEquals(result.data, serialized.data)

    def test_list_sender_blacklist_no_auth(self):
        result = self.noauth_client.get('/api/sender-blacklist/')
        self.assertEquals(result.status_code, 403)

    def test_list_sender_blacklist_auth(self):
        result = self.auth_client.get('/api/sender-blacklist/')
        self.assertEquals(result.status_code, 200)

        serialized = SenderBlacklistSerializer(SenderBlacklist.objects.all(), many=True)
        self.assertEquals(result.data, serialized.data)

    # TODO: Add more tests for blacklists, add, delete, change!
