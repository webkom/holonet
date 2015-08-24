from django.apps import AppConfig
from django.conf import settings

from holonet.storage import backend

from . import get


class DataConfig(AppConfig):

    name = 'holonet.storage'
    verbose_name = 'storage'

    def ready(self):
        super().ready()

        storage_backend_cls = get(settings.STORAGE_BACKEND)
        backend.storage_backend = storage_backend_cls()
        backend.storage_backend.configure()
