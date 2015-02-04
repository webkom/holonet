# -*- coding: utf8 -*-

from rest_framework import mixins, viewsets

from .models import DomainBlacklist, SenderBlacklist
from .serializers import DomainBlacklistSerializer, SenderBlacklistSerializer


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
