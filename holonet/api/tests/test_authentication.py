import mock
from django.test import TestCase

from holonet.api.authentication import HolonetAPIUser, HolonetAuthentication


class APIAuthenticationTestCase(TestCase):

    user_mock = mock.Mock()

    def setUp(self):
        self.auth = HolonetAuthentication()

    @mock.patch('holonet.api.authentication.HolonetAPIUser', return_value=user_mock)
    @mock.patch('oauth2_provider.ext.rest_framework.OAuth2Authentication.authenticate',
                return_value=(None, 'token'))
    def test_api_authenticator_valid_token(self, mock_authenticate, mock_holonet_user):
        token_validation = self.auth.authenticate(None)
        user, token = token_validation
        self.assertEqual(user, self.user_mock)
        self.assertEqual(token, 'token')

        mock_authenticate.assert_called_once_with(None)
        mock_holonet_user.assert_called_once_with()

    @mock.patch('oauth2_provider.ext.rest_framework.OAuth2Authentication.authenticate',
                return_value=None)
    def test_api_authenticator_invalid_token(self, mock_authenticate):
        token_validation = self.auth.authenticate(None)
        self.assertIsNone(token_validation)

        mock_authenticate.assert_called_once_with(None)


class HolonetAPIUserTestCase(TestCase):

    def setUp(self):
        self.user = HolonetAPIUser()

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'HolonetAPI')

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), self.user.get_full_name())
        self.assertEqual(self.user.get_short_name(), 'HolonetAPI')

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), self.user.get_full_name())
        self.assertEqual(self.user.get_username(), 'HolonetAPI')

    def test_has_perm(self):
        self.assertFalse(self.user.has_perm('test_perm'))

    def test_has_perms(self):
        self.assertFalse(self.user.has_perms(['test1', 'test2']))

    @mock.patch('holonet.api.authentication.HolonetAPIUser.has_perm', return_value=True)
    def test_has_perms_true(self, mock_has_perm):
        self.assertTrue(self.user.has_perms(['test1', 'test2']))

    @mock.patch('django.contrib.auth.models._user_has_module_perms', return_value=True)
    def test_has_module_perms(self, mock_user_has_module_perms):
        self.assertTrue(self.user.has_module_perms('test_module'))
        mock_user_has_module_perms.assert_called_once_with(self.user, 'test_module')
