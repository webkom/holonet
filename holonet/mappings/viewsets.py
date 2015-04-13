# -*- coding: utf8 -*-

from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from holonet.mappings.models import MailingList, Recipient

from .helpers import (LookupAddress, clean_address, is_managed_domain, lookup, reverse_lookup,
                      split_address)
from .serializers import LookupSerializer, MailingListSerializer, RecipientSerializer


class PKAndTagViewSet(GenericAPIView):

    lookup_field = 'tag'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            query_value = self.kwargs['tag']

            try:

                query_value = int(query_value)
                obj = queryset.get(Q(pk=query_value) | Q(tag=query_value))

            except ValueError:
                obj = queryset.get(tag=query_value)

        except (queryset.model.DoesNotExist, MultipleObjectsReturned):
            raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
        return obj


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


class RecipientViewSet(viewsets.ModelViewSet, PKAndTagViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class MailingListViewSet(viewsets.ModelViewSet, PKAndTagViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
