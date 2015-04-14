# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import (DomainBlacklistViewSet, DomainWhitelistViewSet,
                                   SenderBlacklistViewSet, SenderWhitelistViewSet)
from holonet.dashboard.viewsets import GraphViewSet, ProcessedViewSet
from holonet.mappings.viewsets import LookupViewSet, MailingListViewSet, RecipientViewSet
from holonet.restricted.viewsets import RestrictedMappingViewSet
from holonet.status.viewsets import StatusViewSet

from .viewsets import InformationViewSet

router = routers.DefaultRouter()
router.register(r'information', InformationViewSet, base_name='information')
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)
router.register(r'sender-whitelist', SenderWhitelistViewSet)
router.register(r'domain-whitelist', DomainWhitelistViewSet)
router.register(r'status', StatusViewSet, base_name='status')
router.register(r'lookup', LookupViewSet, base_name='lookup')
router.register(r'graph', GraphViewSet, base_name='graph')
router.register(r'processed', ProcessedViewSet, base_name='processed')

router.register('recipient', RecipientViewSet)
router.register('mailinglist', MailingListViewSet)
router.register('restricted', RestrictedMappingViewSet)
