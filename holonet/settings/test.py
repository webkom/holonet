# -*- coding: utf8 -*-

MASTER_DOMAINS = [
    'test.holonet.no'
]

TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

ELASTICSEARCH = [
    {'host': '127.0.0.1', 'port': 9200, 'use_ssl': False},
]
