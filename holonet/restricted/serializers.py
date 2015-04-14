# -*- coding: utf8 -*-
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from holonet.mappings.models import Recipient
from holonet.mappings.serializers import RecipientSerializer
from holonet.restricted.models import RestrictedMapping


class RestrictedMappingSerializer(serializers.ModelSerializer):
    """
    This class is used by the /restricted/ endpoint when we lists and retrieve restricted mappings
    """

    recipient_list = RecipientSerializer(many=True)

    class Meta:
        model = RestrictedMapping
        fields = (
            'from_address',
            'is_used',
            'token',
            'valid_from',
            'valid_to',
            'recipient_list',
            'tag',
        )


class RestrictedMappingCreateAndUpdateSerializer(RestrictedMappingSerializer):
    """
    This class is used by the /restricted/ endpoint when we create and update restricted mappings
    """

    recipient_list = SlugRelatedField(
        many=True,
        slug_field='tag',
        queryset=Recipient.objects.all()
    )
