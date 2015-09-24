from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class InfoCommandTestCase(TestCase):

    def test_info(self):
        """
        This is a simple smoke test. Check if the command exist.
        """
        call_command('info', stdout=StringIO())
