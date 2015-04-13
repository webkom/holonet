# -*- coding: utf8 -*-
from rest_framework import serializers

from holonet.mappings.serializers import RecipientSerializer
from holonet.restricted.models import RestrictedMapping


class RestrictedMappingSerializer(serializers.ModelSerializer):

    recipient_list = RecipientSerializer

    class Meta:
        model = RestrictedMapping
