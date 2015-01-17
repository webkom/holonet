# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from django.shortcuts import Http404
from django.conf import settings

from .serializers import ReverseLookupSerializer
from .models import MailingList
from .helpers import ReverseLookupAddress


class ReverseLookupViewSet(viewsets.ViewSet):

    @list_route(methods=['post'])
    def lookup(self, request, *args, **kwargs):
        serializer = ReverseLookupSerializer(data=request.data)
        serializer.is_valid()

        email = serializer.data.get('email')

        if email is None:
            raise Http404('Please attach a email in the request.')

        local = email
        domain = settings.MASTER_DOMAINS[0]
        if '@' in email:
            try:
                local, domain = email.split('@')
            except ValueError:
                raise Http404('Could not find recipients, invalid email.')

        if domain not in settings.MASTER_DOMAINS:
            raise Http404('The domain %s is not handled by Holonet.' % domain)

        recipients = []

        try:
            recipients = MailingList.objects.get(prefix=local).recipients
        except MailingList.DoesNotExist:
            # Check SYSTEM_ALIASES, if ok, send to system admins.
            if local in settings.SYSTEM_ALIASES:
                recipients = [address[1] for address in settings.ADMINS]

        def create_reverse_objects(email):
            return ReverseLookupAddress(email)

        object_recipients = map(create_reverse_objects, recipients)

        serializer = ReverseLookupSerializer(data=object_recipients, many=True)
        serializer.is_valid()

        return Response(serializer.data)


