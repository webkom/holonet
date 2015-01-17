# -*- coding: utf8 -*-

from rest_framework import serializers


class ReverseLookupSerializer(serializers.Serializer):
    email = serializers.EmailField()
