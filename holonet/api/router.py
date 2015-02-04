# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import DomainBlacklistViewSet, SenderBlacklistViewSet
from holonet.dashboard.viewsets import GraphViewSet
from holonet.mappings.viewsets import LookupViewSet
from holonet.restricted.viewsets import RestrictedMappingViewSet
from holonet.status.viewsets import StatusViewSet

from .viewsets import InformationViewSet

router = routers.DefaultRouter()
router.register(r'information', InformationViewSet, base_name='information')
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)
router.register(r'status', StatusViewSet, base_name='status')
router.register(r'lookup', LookupViewSet, base_name='lookup')
router.register(r'graph', GraphViewSet, base_name='graph')
router.register(r'restricted', RestrictedMappingViewSet)
