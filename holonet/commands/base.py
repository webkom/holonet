import logging

from django.core.management.base import BaseCommand

from holonet.settings.version import HOLONET_VERSION

log = logging.getLogger('commands')


class BaseCommand(BaseCommand):

    def handle(self, *args, **options):
        description = 'Mail Delivery System'
        log.info('Holonet v{0} / {1}'.format(HOLONET_VERSION, description))
