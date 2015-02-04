# -*- coding: utf8 -*-

from rest_framework import viewsets

from .models import RestrictedMapping
from .serializers import RestrictedMappingSerializer


class RestrictedMappingViewSet(viewsets.ModelViewSet):

    queryset = RestrictedMapping.objects.active()
    serializer_class = RestrictedMappingSerializer
