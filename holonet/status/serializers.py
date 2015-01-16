# -*- coding: utf8 -*-

from rest_framework import serializers

from holonet.status import BaseStatusClass


class StatusSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    status = serializers.IntegerField(max_value=len(BaseStatusClass.STATUSES))
