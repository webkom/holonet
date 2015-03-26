# -*- coding: utf8 -*-

from django.conf import settings
from django.test import TestCase

from holonet.core.management.commands.sasl_authentication import HolonetSASLHandler


class SASLAuthenticationTestCase(TestCase):

    fixtures = ['users.yaml']

    def setUp(self):
        self.handler = HolonetSASLHandler()

    def test_constants(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_HELLO, 'H')
        self.assertEqual(self.handler.DICT_PROTOCOL_CMD_LOOKUP, 'L')

        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_OK, 'O')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, 'N')
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_FAIL, 'F')

    def test_success(self):
        self.assertEqual('O{}', self.handler.success({}))

    def test_not_found(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_NOTFOUND, self.handler.not_found())

    def test_fail(self):
        self.assertEqual(self.handler.DICT_PROTOCOL_REPLY_FAIL, self.handler.failure())

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

    def test_user_lookup_not_active_user(self):
        user = self.handler.user_lookup('testuser4')
        self.assertIsNone(user)

    def test_user_lookup_ok(self):
        user = self.handler.user_lookup('testuser3')
        self.assertEqual(user.get_sasl_token(), 'KXWKY9C1QKXUE41SMRFFUBHWMSOPAAQX')

    def test_user_lookup_invalid_token(self):
        user = self.handler.user_lookup('testuser2')
        self.assertIsNone(user)

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

    def test_consider_invalid_user(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/userdb/holonet']),
            self.handler.DICT_PROTOCOL_REPLY_NOTFOUND
        )

    def test_consider_userdb_lookup(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/userdb/testuser3']),
            self.handler.success(self.handler.userdb_payload())
        )

    def test_consider_passdb_lookup(self):
        self.assertEqual(
            self.handler.consider(['H2\t0\t0\tholonet', 'Lshared/passdb/testuser3']),
            self.handler.success(self.handler.passdb_payload('KXWKY9C1QKXUE41SMRFFUBHWMSOPAAQX'))
        )
