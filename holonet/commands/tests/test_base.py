from io import StringIO

from django.test import TestCase

from holonet.commands.base import BaseCommand


class BaseCommandTestCase(TestCase):

    def setUp(self):
        self.command = BaseCommand(stdout=StringIO())

    def test_handle(self):
        """
        This is a simple smoke test.
        """
        self.command.handle()
