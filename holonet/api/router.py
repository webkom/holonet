# -*- coding: utf8 -*-

from rest_framework import routers

from holonet.core.viewsets import SenderBlacklistViewSet, DomainBlacklistViewSet


router = routers.DefaultRouter()
router.register(r'sender-blacklist', SenderBlacklistViewSet)
router.register(r'domain-blacklist', DomainBlacklistViewSet)
