from django.test import Client, TestCase

from holonet.api.models import Token
from holonet.core.models import DomainWhitelist, SenderWhitelist
from holonet.core.serializers import DomainWhitelistSerializer, SenderWhitelistSerializer


class WhitelistAPITestCase(TestCase):
    fixtures = ['whitelist.yaml', 'applications.yaml', 'tokens.yaml']

    def setUp(self):

        self.auth_client = Client(HTTP_AUTHORIZATION=Token.objects.first().token)
        self.noauth_client = Client()

    def test_list_domain_whitelist_no_auth(self):
        result = self.noauth_client.get('/api/domain-whitelist/')
        self.assertEquals(result.status_code, 403)

    def test_list_domain_whitelist_auth(self):
        result = self.auth_client.get('/api/domain-whitelist/')
        self.assertEquals(result.status_code, 200)

        serialized = DomainWhitelistSerializer(DomainWhitelist.objects.all(), many=True)
        self.assertEquals(result.data, serialized.data)

    def test_list_sender_whitelist_no_auth(self):
        result = self.noauth_client.get('/api/sender-whitelist/')
        self.assertEquals(result.status_code, 403)

    def test_list_sender_whitelist_auth(self):
        result = self.auth_client.get('/api/sender-whitelist/')
        self.assertEquals(result.status_code, 200)

        serialized = SenderWhitelistSerializer(SenderWhitelist.objects.all(), many=True)
        self.assertEquals(result.data, serialized.data)

    # TODO: Add more tests for blacklists, add, delete, change!
