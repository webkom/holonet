# -*- coding: utf8 -*-
from rest_framework import viewsets

from holonet.mappings.viewsets import PKAndTagViewSet
from holonet.restricted.models import RestrictedMapping
from holonet.restricted.serializers import RestrictedMappingSerializer


class RestrictedMappingViewSet(viewsets.ModelViewSet, PKAndTagViewSet):
    queryset = RestrictedMapping.objects.all()
    serializer_class = RestrictedMappingSerializer
