# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist


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


class SenderWhitelistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SenderWhitelist
        fields = (
            'id',
            'sender'
        )


class DomainWhitelistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DomainWhitelist
        fields = (
            'id',
            'domain',
        )
