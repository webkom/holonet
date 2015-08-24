from rest_framework import viewsets

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist
from .serializers import (DomainBlacklistSerializer, DomainWhitelistSerializer,
                          SenderBlacklistSerializer, SenderWhitelistSerializer)


class SenderBlacklistViewSet(viewsets.ModelViewSet):
    queryset = SenderBlacklist.objects.all()
    serializer_class = SenderBlacklistSerializer


class DomainBlacklistViewSet(viewsets.ModelViewSet):
    queryset = DomainBlacklist.objects.all()
    serializer_class = DomainBlacklistSerializer


class SenderWhitelistViewSet(viewsets.ModelViewSet):
    queryset = SenderWhitelist.objects.all()
    serializer_class = SenderWhitelistSerializer


class DomainWhitelistViewSet(viewsets.ModelViewSet):
    queryset = DomainWhitelist.objects.all()
    serializer_class = DomainWhitelistSerializer
