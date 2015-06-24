from django.test import TestCase

from holonet.status import BaseStatusClass, ElasticsearchStatus


class BaseStatusClassTestCase(TestCase):

    def setUp(self):
        self.base_class = BaseStatusClass()

    def test_name(self):
        with self.assertRaises(NotImplementedError):
            self.base_class.name()

    def test_status(self):
        with self.assertRaises(NotImplementedError):
            self.base_class.status()


class ElasticsearchStatusTestCase(TestCase):

    def test_name(self):
        elasticsearch = ElasticsearchStatus()
        self.assertEqual(elasticsearch.name, 'elasticsearch')

    def test_status(self):
        elasticsearch = ElasticsearchStatus()
        self.assertFalse(elasticsearch.status())
