import json

from django.conf import settings
from django.test import TestCase

from holonet.core.management.commands.sasl_authentication import Handler


class SASLAuthenticationTestCase(TestCase):

    fixtures = ['users.yaml']

    def setUp(self):
        self.handler = Handler()

    def test_constants(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_HELLO, 'H')
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_LOOKUP, 'L')

        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_OK, 'O')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, 'N')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_FAIL, 'F')
        self.assertEqual(self.handler.DICT_PROTOCOL_HOLONET_TEST_RESPONSE, 'T')

    def test_success(self):
        self.assertEqual('O{}', self.handler.success({}))

    def test_not_found(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, self.handler.not_found())

    def test_fail(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_FAIL, self.handler.failure())

    def test_test(self):
        self.assertEqual('%s%s' % (self.handler.DICT_PROTOCOL_HOLONET_TEST_RESPONSE,
                                   json.dumps({'content': 'holonet/test'})),
                         self.handler.test({'content': 'holonet/test'}))

    def test_userdb_payload(self):
        self.assertDictEqual(
            {
                'home': settings.SASL_LUSER_HOME,
                'uid': settings.SASL_LUSER_UID,
                'gid': settings.SASL_LUSER_GID
            },
            self.handler.userdb_payload()
        )

    def test_passdb_payload(self):
        password = 'secret'

        self.assertDictEqual(
            {
                'password': password,
                'userdb_home': settings.SASL_LUSER_HOME,
                'userdb_uid': settings.SASL_LUSER_UID,
                'userdb_gid': settings.SASL_LUSER_GID
            },
            self.handler.passdb_payload(password)
        )

    def test_consider_test(self):
        self.assertEqual(
            self.handler.consider(['Tholonet/test']),
            '%s%s' % (self.handler.DICT_PROTOCOL_HOLONET_TEST_RESPONSE,
                      json.dumps({'content': 'holonet/test'}))
        )

    def test_consider_invalid(self):
        self.assertEqual(self.handler.consider([]), self.handler.DICT_PROTOCOL_REPLY_NOTFOUND)

    def test_consider_short_lookup_line(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'L']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lsh']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_invalid_name_space(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lprivate/userdb/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_invalid_query_string(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/passdb/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_invalid_user_login(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/passdb/holonet/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_deactivated_user(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/passdb/testuser2/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_activate_user(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/passdb/testuser1/holonet']),
            self.handler.success(self.handler.passdb_payload('holonet'))
        )

    def test_consider_domain_login(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet',
                                   'Lshared/passdb/testuser1@test.holonet.no/holonet']),
            self.handler.success(self.handler.passdb_payload('holonet'))
        )

    def test_consider_domain_login_unknown_domain(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet',
                                   'Lshared/passdb/testuser1@unknown.holonet.no/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )
