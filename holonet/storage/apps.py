from django.apps import AppConfig

from . import get_storage_backend


class DataConfig(AppConfig):

    name = 'holonet.storage'
    verbose_name = 'storage'

    def ready(self):
        super().ready()

        storage_backend = get_storage_backend()
        storage_backend.configure()
