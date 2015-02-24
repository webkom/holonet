# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import MailingList, Recipient


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecipientResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = (
            'id',
            'address',
            'tag'
        )


class RecipientListSerializer(serializers.Serializer):

    tag = serializers.CharField(max_length=100)

    class Meta:
        fields = (
            'tag',
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


class MappingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MailingList
        fields = (
            'id',
            'prefix',
            'recipients',
            'tag'
        )
