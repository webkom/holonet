# -*- coding: utf8 -*-

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

    def test_status_no_server(self):

        server_config = [
            {'host': '127.0.0.1', 'port': 10000, 'use_ssl': False},
        ]

        with self.settings(ELASTICSEARCH=server_config):
            elasticsearch = ElasticsearchStatus()
            self.assertFalse(elasticsearch.status())

    def test_status(self):
        elasticsearch = ElasticsearchStatus()
        self.assertTrue(isinstance(elasticsearch.status(), bool))
