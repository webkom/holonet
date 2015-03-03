# -*- coding: utf8 -*-

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .helpers import (LookupAddress, clean_address, is_managed_domain, lookup, reverse_lookup,
                      split_address)
from .models import MailingList, Recipient
from .serializers import (LookupSerializer, MappingRecipientSerializer, MappingSerializer,
                          RecipientSerializer)


class TagLookupViewSet():
    @detail_route(methods=['get'])
    def tag(self, request, pk):
        """
        This method is used for lookup by tag. Use the id if you want to do something with the
        object.
        """
        object = get_object_or_404(self.get_queryset().model, tag=pk)
        serializer = self.get_serializer(object)
        return Response(serializer.data)


class RecipientChangeViewSet():
    @detail_route(methods=['get', 'post', 'delete'])
    def recipients(self, request, pk):
        mapping = get_object_or_404(self.get_queryset().model, pk=pk)

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid()

        def get_tag(serializer_element):
            return serializer_element['tag']

        recipient_tags = map(get_tag, serializer.validated_data)
        recipients = Recipient.objects.filter(tag__in=recipient_tags)

        if request.method == 'POST':
            for recipient in recipients:
                mapping.recipient_list.add(recipient)

        elif request.method == 'DELETE':
            for recipient in recipients:
                mapping.recipient_list.remove(recipient)

        result_serializer = MappingRecipientSerializer(mapping.recipient_list, many=True)

        return Response(result_serializer.data)


class LookupViewSet(viewsets.ViewSet):

    @list_route(methods=['post'])
    def lookup(self, request, *args, **kwargs):
        serializer = LookupSerializer(data=request.data)
        serializer.is_valid()

        email = serializer.data.get('email')

        if email is None:
            return Response([])
        else:
            email = clean_address(email)

        prefix, domain = split_address(email)

        if not is_managed_domain(domain):
            return Response([])

        recipients = lookup(prefix)

        def create_lookup_objects(email):
            return LookupAddress(email)

        object_recipients = map(create_lookup_objects, recipients)

        serializer = LookupSerializer(data=object_recipients, many=True)
        serializer.is_valid()

        return Response(serializer.data)

    @list_route(methods=['post'])
    def reverse(self, request, *args, **kwargs):
        serializer = LookupSerializer(data=request.data)
        serializer.is_valid()

        email = serializer.data.get('email')

        if email is None:
            return Response([])

        lists = reverse_lookup(email)

        def create_reverse_objects(prefix):
            return LookupAddress('%s@%s' % (prefix, settings.MASTER_DOMAIN))

        object_lists = map(create_reverse_objects, lists)

        serializer = LookupSerializer(data=object_lists, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class MappingViewSet(viewsets.ModelViewSet, TagLookupViewSet, RecipientChangeViewSet):

    queryset = MailingList.objects.all()
    serializer_class = MappingSerializer


class RecipientViewSet(viewsets.ModelViewSet, TagLookupViewSet):

    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
