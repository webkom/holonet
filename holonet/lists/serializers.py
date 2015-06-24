# -*- coding: utf8 -*-

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from holonet.lists.models import MailingList, Recipient


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecipientSerializer(serializers.ModelSerializer):
    """
    This class is used by the /recipient/ endpoint
    """

    class Meta:
        model = Recipient
        fields = (
            'address',
            'tag'
        )


class MailingListSerializer(serializers.ModelSerializer):
    """
    This class is used by the /mailinglist/ endpoint when we lists and retrieve mappings
    """

    recipient_list = RecipientSerializer(many=True)

    class Meta:
        model = MailingList
        fields = (
            'prefix',
            'recipient_list',
            'tag'
        )


class MailingListCreateAndUpdateSerializer(MailingListSerializer):
    """
    This class is used by the /mailinglist/ endpoint when we create and update mappings
    """

    recipient_list = SlugRelatedField(
        many=True,
        slug_field='tag',
        queryset=Recipient.objects.all()
    )
