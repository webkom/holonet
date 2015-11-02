import certifi
from django.conf import settings
from elasticsearch_dsl.connections import connections

from holonet.interfaces.storage_provider import StorageProvider


class ElasticsearchProvider(StorageProvider):

    def set_up(self):
        connections.configure(
            default={
                'hosts': settings.ELASTICSEARCH,
                'verify_certs': True,
                'ca_certs': certifi.where(),
                'timeout': 60.0,
            },
        )

elasticsearch_provider = ElasticsearchProvider()
