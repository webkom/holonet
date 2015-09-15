from rest_framework import serializers

from holonet.interfaces.storage_backend import StorageBackend


class StoredEmailSerializer(serializers.Serializer):

    timestamp = serializers.DateTimeField()
    from_email = serializers.CharField()
    to = serializers.ListField(child=serializers.CharField())
    copy = serializers.ListField(child=serializers.CharField())
    blind_copy = serializers.ListField(child=serializers.CharField())
    recipients = serializers.ListField(child=serializers.CharField())
    subject = serializers.CharField()
    raw = serializers.CharField()
    type = serializers.CharField()


class StoredEmailFilterSerializer(serializers.Serializer):
    time_from = serializers.DateTimeField()
    time_to = serializers.DateTimeField()
    filter = serializers.ListField(child=serializers.CharField(), required=False,
                                   default=StorageBackend.MESSAGE_TYPES_LIST)
    search_query = serializers.CharField(required=False, default=None)
