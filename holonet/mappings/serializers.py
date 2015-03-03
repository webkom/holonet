# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import MailingList, Recipient


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class MappingRecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = (
            'id',
            'address',
            'tag'
        )


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = (
            'id',
            'address',
            'tag',
            'lists'
        )


class MappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailingList
        fields = (
            'id',
            'prefix',
            'recipients',
            'tag'
        )
