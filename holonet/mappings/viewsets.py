# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .serializers import LookupSerializer
from .helpers import LookupAddress, clean_address, lookup, split_address, is_managed_domain


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

        def create_reverse_objects(email):
            return LookupAddress(email)

        object_recipients = map(create_reverse_objects, recipients)

        serializer = LookupSerializer(data=object_recipients, many=True)
        serializer.is_valid()

        return Response(serializer.data)
