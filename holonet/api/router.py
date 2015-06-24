# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import (DomainBlacklistViewSet, DomainWhitelistViewSet,
                                   SenderBlacklistViewSet, SenderWhitelistViewSet)
from holonet.lists.viewsets import LookupViewSet, MailingListViewSet, RecipientViewSet
from holonet.restricted.viewsets import RestrictedMappingViewSet
from holonet.status.viewsets import StatusViewSet
from holonet.storage.viewsets import EmailStoreViewSet

from .viewsets import InformationViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'information', InformationViewSet, base_name='information')
router.register(r'tasks', TaskViewSet, base_name='tasks')
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)
router.register(r'sender-whitelist', SenderWhitelistViewSet)
router.register(r'domain-whitelist', DomainWhitelistViewSet)
router.register(r'status', StatusViewSet, base_name='status')
router.register(r'lookup', LookupViewSet, base_name='lookup')

router.register('recipient', RecipientViewSet)
router.register('mailinglist', MailingListViewSet)
router.register('restricted', RestrictedMappingViewSet)

router.register('email-store', EmailStoreViewSet, base_name='email-store')
