# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import RestrictedMapping


class RestrictedMappingSerializer(serializers.HyperlinkedModelSerializer):

    token = serializers.CharField(max_length=64, allow_blank=True, allow_null=True)

    class Meta:
        model = RestrictedMapping
        fields = (
            'token',
            'valid_from',
            'valid_to',
            'from_address',
            'recipients'
        )
