from django.apps import AppConfig

from .utils import fetch_queue


class DataConfig(AppConfig):

    name = 'holonet.queue'
    verbose_name = 'queue'

    def ready(self):
        super().ready()
        fetch_queue().setup()
