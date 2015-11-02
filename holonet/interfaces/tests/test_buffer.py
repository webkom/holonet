from datetime import datetime

import pytz
from django.test import TestCase
from rest_framework import serializers

from holonet.interfaces.buffer import Buffer


class BufferTestSerializer(serializers.Serializer):
    title = serializers.CharField()
    timestamp = serializers.DateTimeField()


TEST_PAYLOAD = {
    'title': 'Buffer Test',
    'timestamp': datetime(year=2000, month=1, day=1, hour=12, minute=0, tzinfo=pytz.UTC)
}
TEST_PAYLOAD_SERIALIZED = '{"title":"Buffer Test","timestamp":"2000-01-01T12:00:00Z"}'.encode()


class BufferTestCase(TestCase):

    def setUp(self):
        self.buffer = Buffer()

    def test_create_key(self):
        payload = 'payload'.encode()
        key = self.buffer.create_key(payload)
        self.assertEquals(len(key), 32)
        self.assertEquals(type(key), str)

    def test_serialize_object(self):
        raw_stream = self.buffer.serialize_object(TEST_PAYLOAD, BufferTestSerializer)

        self.assertEquals(type(raw_stream), bytes)

        # Also make sure we can create a key based on the output
        key = self.buffer.create_key(raw_stream)
        self.assertEquals(type(key), str)
        self.assertEquals(len(key), 32)

    def test_deserialize_data(self):
        payload_object = self.buffer.deserialize_object(TEST_PAYLOAD_SERIALIZED,
                                                        BufferTestSerializer)
        self.assertDictEqual(payload_object, TEST_PAYLOAD)

    def test_serialize_value_error(self):
        self.assertRaises(ValueError, self.buffer.serialize_object, {}, BufferTestSerializer)

    def test_deserialize_value_error(self):
        self.assertRaises(ValueError, self.buffer.deserialize_object, '{"key": "value"}'.encode(),
                          BufferTestSerializer)
