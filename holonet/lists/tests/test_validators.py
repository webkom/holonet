# -*- coding: utf8 -*-

from django.core.validators import ValidationError
from django.test import TestCase

from holonet.lists.validators import validate_local_part


class ValidatorsTestCase(TestCase):
    def test_validate_local_part(self):
        self.assertRaises(ValidationError, validate_local_part, value='!#$%*/?^`{|}~€')
