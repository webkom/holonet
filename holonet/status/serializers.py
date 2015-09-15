from rest_framework import serializers

from holonet.interfaces.status_check import StatusCheck


class StatusSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    status = serializers.IntegerField(max_value=len(StatusCheck.STATUSES))
