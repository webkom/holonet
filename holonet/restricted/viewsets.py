# -*- coding: utf8 -*-

from rest_framework import viewsets

from .serializers import RestrictedMappingSerializer
from .models import RestrictedMapping


class RestrictedMappingViewSet(viewsets.ModelViewSet):

    queryset = RestrictedMapping.objects.active()
    serializer_class = RestrictedMappingSerializer
