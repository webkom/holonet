from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .helpers import (LookupAddress, clean_address, is_managed_domain, lookup, reverse_lookup,
                      split_address)
from .models import MailingList, Recipient
from .serializers import (LookupSerializer, MailingListCreateAndUpdateSerializer,
                          MailingListSerializer, RecipientSerializer)


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


class RecipientViewSet(viewsets.ModelViewSet):
    lookup_field = 'tag'
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class MailingListViewSet(viewsets.ModelViewSet):
    lookup_field = 'tag'
    queryset = MailingList.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return MailingListCreateAndUpdateSerializer
        return MailingListSerializer
