from holonet.common.manager import ServiceManager
from .backends import elasticsearch, database

default_app_config = 'holonet.storage.apps.DataConfig'


manager = ServiceManager()
manager.add('database', database.Backend)
manager.add('elasticsearch', elasticsearch.Backend)

get = manager.get
