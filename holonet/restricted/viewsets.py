# -*- coding: utf8 -*-

from rest_framework import viewsets

from holonet.mappings.viewsets import RecipientChangeViewSet, TagLookupViewSet

from .models import RestrictedMapping
from .serializers import RestrictedMappingSerializer


class RestrictedMappingViewSet(viewsets.ModelViewSet, TagLookupViewSet, RecipientChangeViewSet):

    queryset = RestrictedMapping.objects.active()
    serializer_class = RestrictedMappingSerializer
