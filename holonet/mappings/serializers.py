# -*- coding: utf8 -*-

from rest_framework import serializers

from .models import Recipient


class LookupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
