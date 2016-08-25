import logging

from holonet.apps.utils.base_service import Service

log = logging.getLogger(__name__)


class AuthSocket(Service):
    """
    """

    name = 'auth_socket'
    help = 'Start a socket for Dovecot dict auth'
    log = log

    def run(self, *args, **kwargs):
        pass

    def close(self):
        pass

    def __init__(self):
        self.log.info('Starting auth socket')
        super().__init__()
