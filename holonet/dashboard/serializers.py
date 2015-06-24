from rest_framework import serializers


class GraphRequestSerializer(serializers.Serializer):
    query = serializers.CharField(default='', max_length=255)

    time_from = serializers.IntegerField(default=0)
    time_to = serializers.IntegerField(default=0)

    spam = serializers.BooleanField()
    bounce = serializers.BooleanField()
    blacklisted = serializers.BooleanField()


class ProcessedRequestSerializer(serializers.Serializer):
    time_from = serializers.IntegerField(default=0)
    time_to = serializers.IntegerField(default=0)
