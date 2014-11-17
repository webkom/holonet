# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import SenderBlacklistViewSet, DomainBlacklistViewSet
from holonet.mappings.viewsets import MailingListViewSet, RecipientViewSet


router = routers.DefaultRouter()
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)

router.register(r'lists', MailingListViewSet)
router.register(r'recipients', RecipientViewSet)
