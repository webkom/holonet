# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import SenderBlacklistSerializer, DomainBlacklistSerializer
from .models import SenderBlacklist, DomainBlacklist


class SenderBlacklistViewSet(viewsets.ModelViewSet):
    queryset = SenderBlacklist.objects.all()
    serializer_class = SenderBlacklistSerializer
    permission_classes = (IsAuthenticated, )


class DomainBlacklistViewSet(viewsets.ModelViewSet):
    queryset = DomainBlacklist.objects.all()
    serializer_class = DomainBlacklistSerializer
    permission_classes = (IsAuthenticated, )
