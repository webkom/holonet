from django.apps import AppConfig


class DataConfig(AppConfig):

    name = 'holonet.core'
    verbose_name = 'core'

    def ready(self):
        super().ready()
