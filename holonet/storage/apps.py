from django.apps import AppConfig
from django.conf import settings

from .buffer import load_buffer
from .providers.elasticsearch_provider import elasticsearch_provider
from .providers.redis_provider import redis_provider


class DataConfig(AppConfig):
    name = 'holonet.storage'
    verbose_name = 'storage'

    def ready(self):
        super(DataConfig, self).ready()

        # Setup storage providers
        redis_provider.set_up()
        elasticsearch_provider.set_up()

        # Setup buffer module
        load_buffer(settings.MESSAGE_BUFFER)
