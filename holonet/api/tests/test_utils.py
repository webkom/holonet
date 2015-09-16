from django.test import TestCase
from mock import mock

from holonet.api import utils


class UtilsTestCase(TestCase):

    def test_base_url(self):
        request = mock.Mock()
        request.get_host = lambda: 'holonet.com'

        request.is_secure = lambda *args, **kwargs: True
        self.assertEqual(utils.base_url(request), 'https://holonet.com')

        request.is_secure = lambda *args, **kwargs: False
        self.assertEqual(utils.base_url(request), 'http://holonet.com')

    @mock.patch('django.core.urlresolvers.reverse', return_value='/reverse')
    def test_reverse(self, mock_reverse):
        self.assertEqual(utils.reverse('name', 'base', 'arg1', kwarg1=True), 'base/reverse')
        mock_reverse.assert_called_once_with('name', 'arg1', kwarg1=True)
