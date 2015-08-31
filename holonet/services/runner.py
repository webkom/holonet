import logging
import signal
import sys
from abc import abstractmethod

from django.core.management import BaseCommand


class Runner(BaseCommand):

    log = logging.getLogger(__name__)
    option_list = BaseCommand.option_list + (

    )

    requires_model_validation = True

    help = "Start Holonet service"
    name = None

    def __init__(self):
        super().__init__()

    def _handle_sigterm(self, signum, frame):
        self.close()
        sys.exit(0)

    def _handle_sigusr1(self, signum, frame):
        self._handle_sigterm(signum, frame)

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

    def handle(self, *args, **kwargs):
        self.log = logging.getLogger('holonet.{}'.format(self.name))

        try:
            # Gracefully exit on sigterm.
            signal.signal(signal.SIGTERM, self._handle_sigterm)

            # A SIGUSR1 signals an exit with an autorestart
            signal.signal(signal.SIGUSR1, self._handle_sigusr1)

            # Handle Keyboard Interrupt
            signal.signal(signal.SIGINT, self._handle_sigterm)

            self.log.info('Starting service {}'.format(self.name))
            self.run(*args, **kwargs)

        except Exception as e:
            self.log.exception(e)
            sys.exit(1)
