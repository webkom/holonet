# -*- coding: utf8 -*-
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import StoredEmailFilterSerializer


class EmailStoreViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({})

    def retrieve(self, request, *args, **kwargs):
        serializer = StoredEmailFilterSerializer(data=request.data)
        serializer.is_valid()

        return Response({})
