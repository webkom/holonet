import hashlib
from abc import abstractmethod

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class Buffer:

    def set_up(self):
        """
        Configure buffer. Called on buffer initialization.
        """
        pass

    @staticmethod
    def serialize_object(payload, serializer_cls):
        """
        Creates a byte-array from a payload serialized with a rest_framework serializer.
        """
        serializer = serializer_cls(data=payload)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            return JSONRenderer().render(validated_data)
        raise ValueError('Could not serialize payload with serializer {}'
                         .format(str(serializer_cls)))

    @staticmethod
    def deserialize_object(payload, serializer_cls):
        """
        Deserialize a byte-array and return a object.
        """
        stream = BytesIO(payload)
        data = JSONParser().parse(stream)
        serializer = serializer_cls(data=data)
        if serializer.is_valid():
            return serializer.validated_data
        raise ValueError('Could not deserialize payload with the serializer {}'
                         .format(str(serializer_cls)))

    @staticmethod
    def create_key(raw_data):
        """
        Create a key based on an byte-array with data
        """
        return hashlib.md5(raw_data).hexdigest()

    @abstractmethod
    def store_payload(self, payload, serializer_cls):
        """
        Store a object in the buffer. Uses a rest_framework serializer to serialize the object.
        Returns a key used by later lookups.
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve_payload(self, key, serializer_cls):
        """
        Return a object based on a key from the buffer. Uses a rest_framework serializer to
        deserialize the payload stored in the buffer.
        If object does not exists, return None.
        """
        raise NotImplementedError

    @abstractmethod
    def purge_payload(self, key):
        """
        Remove a object from the buffer.
        """
        raise NotImplementedError
