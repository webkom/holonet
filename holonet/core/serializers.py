# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import SenderBlacklist, DomainBlacklist


class SenderBlacklistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SenderBlacklist
        fields = (
            'id',
            'sender'
        )


class DomainBlacklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DomainBlacklist
        fields = (
            'id',
            'domain',
        )
