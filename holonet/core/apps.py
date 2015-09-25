from django.apps import AppConfig

from .queue import fetch_queue_runner


class DataConfig(AppConfig):

    name = 'holonet.core'
    verbose_name = 'core'

    def ready(self):
        super().ready()
        fetch_queue_runner().setup()
