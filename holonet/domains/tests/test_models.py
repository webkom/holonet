# -*- coding: utf8 -*-

from django.test import TestCase

from holonet.domains.models import Domain


class ModelTestCase(TestCase):

    fixtures = ['domains.yaml']

    def test_domain_save(self):

        domain_name = 'TestDomain.com'

        domain = Domain(domain=domain_name)
        domain.save()

        self.assertEqual(domain_name.lower(), domain.domain)
        self.assertTrue(domain.domain.islower())

    def test_valid_domain_lookup(self):

        domain = Domain.lookup_domain('Test.com')
        self.assertEqual(domain.domain, 'test.com')

    def test_invalid_lookup(self):

        domain = Domain.lookup_domain('unknown.com')
        self.assertIsNone(domain)

    def test_stringify(self):
        domain_name = 'test.com'
        domain = Domain(domain=domain_name)
        self.assertEqual(domain_name, str(domain))

    def test_list_domains(self):
        domain_list = ['test.com']
        self.assertListEqual(domain_list, Domain.list_domains())
