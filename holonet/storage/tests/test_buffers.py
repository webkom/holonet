from django.test import TestCase
from rest_framework import serializers

from holonet.interfaces.tests.test_buffer import (TEST_PAYLOAD, TEST_PAYLOAD_SERIALIZED,
                                                  BufferTestSerializer)
from holonet.storage.buffer.backends import django_cache, redis


class BufferSerializer(serializers.Serializer):
    version = serializers.IntegerField()


class BufferBaseTestCase:

    def setUp(self):
        # Purge old buffer results
        self.test_key = self.buffer.create_key(TEST_PAYLOAD_SERIALIZED)
        self.buffer.purge_payload(self.test_key)

    def test_backend(self):
        # Try to retrieve invalid key
        none_object = self.buffer.retrieve_payload(self.test_key, BufferTestSerializer)
        self.assertIsNone(none_object)

        # Store a object and validate the key
        stored_key = self.buffer.store_payload(TEST_PAYLOAD, BufferTestSerializer)
        self.assertEquals(stored_key, self.test_key)
        self.assertEquals(len(stored_key), 32)

        # Retrieve object
        retrieved_object = self.buffer.retrieve_payload(self.test_key, BufferTestSerializer)
        self.assertDictEqual(retrieved_object, TEST_PAYLOAD)

        # Purge object
        self.buffer.purge_payload(self.test_key)

        # Try to retrieve purged key
        purged_object = self.buffer.retrieve_payload(self.test_key, BufferBaseTestCase)
        self.assertIsNone(purged_object)

        # Make a key invalid and try to retrieve it
        self.buffer.store_payload(TEST_PAYLOAD, BufferTestSerializer)
        invalid_object = self.buffer.retrieve_payload(self.test_key, BufferSerializer)
        self.assertIsNone(invalid_object)

        # Try to store a invalid object
        self.assertRaises(ValueError, self.buffer.store_payload, TEST_PAYLOAD, BufferSerializer)


class RedisBufferTestCase(BufferBaseTestCase, TestCase):

    def __init__(self, *args, **kwargs):
        self.buffer = redis.RedisBuffer()
        self.buffer.set_up()
        super().__init__(*args, **kwargs)


class DjangoCacheBufferTestCase(BufferBaseTestCase, TestCase):

    def __init__(self, *args, **kwargs):
        self.buffer = django_cache.DjangoCacheBuffer()
        self.buffer.set_up()
        super().__init__(*args, **kwargs)
