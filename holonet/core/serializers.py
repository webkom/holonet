from rest_framework import serializers

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist


class SenderBlacklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = SenderBlacklist


class DomainBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainBlacklist


class SenderWhitelistSerializer(serializers.ModelSerializer):

    class Meta:
        model = SenderWhitelist


class DomainWhitelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainWhitelist
