# -*- coding: utf8 -*-

from rest_framework import serializers


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()
