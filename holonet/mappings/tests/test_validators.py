# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.validators import ValidationError

from holonet.mappings.validators import validate_local_part


class ValidatorsTestCase(TestCase):
    def test_validate_local_part(self):
        self.assertRaises(ValidationError, validate_local_part, value='!#$%*/?^`{|}~€')
