import logging
import signal
import sys
from abc import abstractmethod

from django.core.management import BaseCommand


class Service(BaseCommand):

    log = logging.getLogger(__name__)
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
        raise NotImplementedError

    def handle(self, *args, **kwargs):
        try:
            # Gracefully exit on sigterm.
            signal.signal(signal.SIGTERM, self._handle_sigterm)

            # A SIGUSR1 signals an exit with an autorestart
            signal.signal(signal.SIGUSR1, self._handle_sigusr1)

            # Handle Keyboard Interrupt
            signal.signal(signal.SIGINT, self._handle_sigterm)

            self.run(*args, **kwargs)

        except Exception:
            self.log.exception('Fatal service exception, exiting')
            sys.exit(1)
