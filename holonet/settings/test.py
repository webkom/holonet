# -*- coding: utf8 -*-

MASTER_DOMAINS = [
    'test.holonet.no'
]

ELASTICSEARCH = [
    {'host': 'prd001.trh.whale.io', 'port': 9200, 'use_ssl': False},
]

TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"
