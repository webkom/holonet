import logging
import sys

from django.conf import settings

from holonet.commands.base import BaseCommand
from holonet.settings.version import HOLONET_VERSION

log = logging.getLogger('commands')


class Command(BaseCommand):

    help = 'Display information about the running Holonet instance.'

    def handle(self, *args, **options):
        super().handle(*args, **options)

        log.info('{0}: {1}'.format('Holonet version', HOLONET_VERSION))
        log.info('{0}: {1}'.format('Python version', sys.version.split(' ')[0]))
        log.info('{0}: {1}'.format('Production mode', not settings.DEBUG))
