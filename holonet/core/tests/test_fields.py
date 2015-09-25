from django.test import TestCase

from holonet.core.fields import DomainField, LocalPartField


class DomainFieldTestCase(TestCase):

    def setUp(self):
        self.field = DomainField()

    def test_clean(self):
        self.assertEqual(self.field.clean('VG.no', None), 'vg.no')

    def test_formfield(self):
        field = self.field.formfield()
        self.assertTrue('invalid' in field.error_messages.keys())


class LocalPartFieldTestCase(TestCase):

    def setUp(self):
        self.field = LocalPartField()

    def test_clean(self):
        self.assertEqual(self.field.clean('HolOnet', None), 'holonet')

    def test_formfield(self):
        field = self.field.formfield()
        self.assertTrue('invalid' in field.error_messages.keys())
