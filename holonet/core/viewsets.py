# -*- coding: utf8 -*-

from rest_framework import mixins, viewsets

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist
from .serializers import (DomainBlacklistSerializer, DomainWhitelistSerializer,
                          SenderBlacklistSerializer, SenderWhitelistSerializer)


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


class SenderWhitelistViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = SenderWhitelist.objects.all()
    serializer_class = SenderWhitelistSerializer


class DomainWhitelistViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = DomainWhitelist.objects.all()
    serializer_class = DomainWhitelistSerializer
