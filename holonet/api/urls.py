from django.conf.urls import include, patterns, url

from .router import router

urlpatterns = patterns(
    'holonet.api',
    url(r'^api/', include(router.urls)),
)
