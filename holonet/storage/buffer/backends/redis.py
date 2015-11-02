from holonet.interfaces.buffer import Buffer
from holonet.storage.providers.redis_provider import redis_provider


class RedisBuffer(Buffer):

    hash_name = 'redis-buffer'
    client = None

    def set_up(self):
        self.client = redis_provider.client

    def store_payload(self, payload, serializer_cls):
        serialized_object = self.serialize_object(payload, serializer_cls)
        key = self.create_key(serialized_object)
        self.client.hset(self.hash_name, key, serialized_object)
        return key

    def retrieve_payload(self, key, serializer_cls):
        stored_payload = self.client.hget(self.hash_name, key)
        if stored_payload:
            try:
                return self.deserialize_object(stored_payload, serializer_cls)
            except ValueError:
                pass

    def purge_payload(self, key):
        return self.client.hdel(self.hash_name, key)
