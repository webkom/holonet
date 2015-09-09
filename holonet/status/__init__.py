from holonet.core.manager import ServiceManager

from holonet.status.backends import elasticsearch, cache

manager = ServiceManager()

manager.add('elasticsearch', elasticsearch.ElasticsearchStatus)
manager.add('cache', cache.CacheStatus)

get = manager.get
choices = manager.choices
