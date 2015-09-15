from holonet.core.manager import ServiceManager

from holonet.status.checks import elasticsearch, cache

manager = ServiceManager()

manager.add('elasticsearch', elasticsearch.ElasticsearchStatus)
manager.add('cache', cache.CacheStatus)

get = manager.get
choices = manager.choices
