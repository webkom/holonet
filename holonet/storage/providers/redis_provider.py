import redis
from django.conf import settings

from holonet.interfaces.storage_provider import StorageProvider


class RedisProvider(StorageProvider):

    def __init__(self):
        self.pool = None
        self.client = None

    def set_up(self):
        self.pool = redis.ConnectionPool(**settings.REDIS)
        self.client = redis.Redis(connection_pool=self.pool)

redis_provider = RedisProvider()
