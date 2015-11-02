from django.core.cache import cache

from holonet.interfaces.buffer import Buffer


class DjangoCacheBuffer(Buffer):

    key_name = 'djbuffer-{}'

    def store_payload(self, payload, serializer_cls):
        serialized_object = self.serialize_object(payload, serializer_cls)
        key = self.create_key(serialized_object)
        cache.set(self.key_name.format(key), serialized_object)
        return key

    def retrieve_payload(self, key, serializer_cls):
        stored_payload = cache.get(self.key_name.format(key))
        if stored_payload:
            try:
                return self.deserialize_object(stored_payload, serializer_cls)
            except ValueError:
                pass

    def purge_payload(self, key):
        return cache.delete(self.key_name.format(key))
