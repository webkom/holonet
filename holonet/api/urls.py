# -*- coding: utf8 -*-

from django.conf.urls import patterns, url, include

from .router import router


urlpatterns = patterns(
    'holonet.api',
    url(r'^api/', include(router.urls)),
)
