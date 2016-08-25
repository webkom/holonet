from unittest import mock

from django.test import TestCase

from holonet.apps.utils.manager import ServiceManager


class ManagerTestCase(TestCase):

    def setUp(self):
        self.manager = ServiceManager()

    def test_add_service(self):

        service_mock = mock.Mock()
        service_mock.func = lambda: True

        self.manager.add('mock', service_mock)

        self.assertTrue('mock' in self.manager._backends.keys())
        self.assertEqual(self.manager._backends.get('mock'), service_mock)

    def test_get_service(self):

        service_mock = mock.Mock()
        service_mock.func = lambda: True

        self.manager._backends['get_test'] = service_mock

        manager_service = self.manager.get('get_test')
        self.assertEqual(manager_service, service_mock)

        self.assertTrue(manager_service.func())

    def test_choises(self):
        self.manager._backends = {}

        self.assertListEqual(self.manager.choices, [])

        self.manager._backends['test'] = None
        self.assertListEqual(self.manager.choices, [('test', 'test')])

    def test_keys(self):
        self.manager._backends = {}

        self.assertListEqual(self.manager.keys(), [])

        self.manager._backends['test'] = None
        self.assertListEqual(self.manager.keys(), ['test'])
