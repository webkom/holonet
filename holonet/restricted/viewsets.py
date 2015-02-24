# -*- coding: utf8 -*-

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from holonet.mappings.models import Recipient
from holonet.mappings.serializers import RecipientListSerializer, RecipientResultSerializer

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

    @detail_route(methods=['get', 'post', 'delete'])
    def recipients(self, request, pk):
        restricted_mapping = get_object_or_404(RestrictedMapping, pk=pk)

        serializer = RecipientListSerializer(data=request.data, many=True)
        serializer.is_valid()

        def get_tag(serializer_element):
            return serializer_element['tag']

        recipient_tags = map(get_tag, serializer.validated_data)
        recipients = Recipient.objects.filter(tag__in=recipient_tags)

        if request.method == 'POST':
            for recipient in recipients:
                restricted_mapping.recipient_list.add(recipient)

        elif request.method == 'DELETE':
            for recipient in recipients:
                restricted_mapping.recipient_list.remove(recipient)

        result_serializer = RecipientResultSerializer(restricted_mapping.recipient_list, many=True)

        return Response(result_serializer.data)
