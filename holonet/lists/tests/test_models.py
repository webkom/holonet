import mock
from django.test import TestCase

from holonet.lists.models import Domain


class DomainModelTestCase(TestCase):

    def test_str(self):
        domain = Domain(domain='holonet.com')
        self.assertEqual(str(domain), 'holonet.com')

    @mock.patch('django.db.models.Model.save')
    def test_save(self, mock_model_save):
        domain = Domain(domain='holonet.com')
        domain.save()
        mock_model_save.assert_called_once_with()

        self.assertEqual(domain.base_url, 'http://holonet.com')
