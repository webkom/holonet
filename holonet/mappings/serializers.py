# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import MailingList


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class MappingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MailingList
        fields = (
            'id',
            'prefix',
            'recipients',
            'tag'
        )
