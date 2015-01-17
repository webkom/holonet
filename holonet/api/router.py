# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import SenderBlacklistViewSet, DomainBlacklistViewSet
from holonet.status.viewsets import StatusViewSet
from holonet.mappings.viewsets import ReverseLookupViewSet


router = routers.DefaultRouter()
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)
router.register(r'status', StatusViewSet, base_name='status')
router.register(r'reverse-lookup', ReverseLookupViewSet, base_name='reverse-lookup')
