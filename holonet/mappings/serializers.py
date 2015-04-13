# -*- coding: utf8 -*-

from rest_framework import serializers

from holonet.mappings.models import MailingList, Recipient


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient


class MailingListSerializer(serializers.ModelSerializer):

    recipient_list = RecipientSerializer

    class Meta:
        model = MailingList
