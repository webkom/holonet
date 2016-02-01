import os

from django.conf import settings


class PostfixTransportMaps:

    def __init__(self):
        self.postmap_command = getattr(settings, 'POSTFIX_POSTMAP_COMMAND', 'postmap')
        self.data_directory = os.path.join(settings.BASE_DIR, 'data')
        self.lmtp_server = '{0}:{1}'.format(settings.LMTP_HOST, settings.LMTP_PORT)

    def generate(self):
        pass
