from django.core.management.base import BaseCommand

from holonet.settings.version import HOLONET_VERSION


class BaseCommand(BaseCommand):

    def handle(self, *args, **options):
        description = 'Mail Delivery System'
        self.stdout.write('Holonet v{} / {}'.format(HOLONET_VERSION, description))
