import sys

from django.conf import settings
from django.core.urlresolvers import reverse

from holonet.commands.base import BaseCommand
from holonet.settings.version import HOLONET_VERSION


class Command(BaseCommand):

    help = 'Display information about the running Holonet instance.'

    def handle(self, *args, **options):
        super().handle(*args, **options)

        self.stdout.write('-' * 60)
        self.stdout.write('{}{}'.format('Holonet version'.ljust(30), HOLONET_VERSION))
        self.stdout.write('{}{}'.format('Python version'.ljust(30), sys.version.split(' ')[0]))
        self.stdout.write('{}{}'.format('Production mode'.ljust(30), not settings.DEBUG))
        self.stdout.write('{}{}'.format('API endpoint'.ljust(30), reverse('api:browse')))
        self.stdout.write('-' * 60)
