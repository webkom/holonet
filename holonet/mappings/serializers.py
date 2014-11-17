# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import MailingList, Recipient


class MailingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = (
            'id',
            'prefix',
        )


class MailingListRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = (
            'id',
            'prefix',
            'recipient_list',
        )


class MailingListRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = (
            'recipient_list',
        )


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = (
            'id',
            'address',
            'tag',
        )
