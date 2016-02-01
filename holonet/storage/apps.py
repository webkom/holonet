from django.apps import AppConfig

from .providers.elasticsearch_provider import elasticsearch_provider


class DataConfig(AppConfig):
    name = 'holonet.storage'
    verbose_name = 'storage'

    def ready(self):
        super(DataConfig, self).ready()

        # Setup storage providers
        elasticsearch_provider.set_up()
