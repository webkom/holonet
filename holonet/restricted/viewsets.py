# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import RestrictedMapping
from .serializers import RestrictedMappingSerializer


class RestrictedMappingViewSet(viewsets.ModelViewSet):

    queryset = RestrictedMapping.objects.active()
    serializer_class = RestrictedMappingSerializer

    @detail_route(methods=['get'])
    def tag(self, request, pk):
        """
        This method is used for lookup by tag. Use the id if you want to do something with the
        object.
        """
        mapping = get_object_or_404(RestrictedMapping, tag=pk)
        serializer = self.get_serializer(mapping)
        return Response(serializer.data)
