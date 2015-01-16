# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework import mixins

from .serializers import SenderBlacklistSerializer, DomainBlacklistSerializer
from .models import SenderBlacklist, DomainBlacklist


class SenderBlacklistViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = SenderBlacklist.objects.all()
    serializer_class = SenderBlacklistSerializer


class DomainBlacklistViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = DomainBlacklist.objects.all()
    serializer_class = DomainBlacklistSerializer
