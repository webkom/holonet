# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import RestrictedMapping


class RestrictedMappingSerializer(serializers.HyperlinkedModelSerializer):

    token = serializers.ReadOnlyField()

    class Meta:
        model = RestrictedMapping
        fields = (
            'id',
            'token',
            'valid_from',
            'valid_to',
            'from_address',
            'recipients',
            'tag'
        )
