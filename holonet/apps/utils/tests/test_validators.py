from django.core.exceptions import ValidationError
from django.test import TestCase

from holonet.apps.utils.validators import domain_validator, local_validator


class DomainValidatorTestCase(TestCase):

    def test_valdate(self):
        self.assertRaises(ValidationError, domain_validator, 'invalid"#$email.com')
        self.assertIsNone(domain_validator('holonet.com'))


class LocalPartValidatorTestCase(TestCase):

    def test_validate(self):
        self.assertRaises(ValidationError, local_validator, 'local@')
        self.assertIsNone(local_validator('holonet'))
