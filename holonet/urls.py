from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('holonet.apps.api.urls', namespace='api')),
    url(r'^manage/', include(admin.site.urls)),
    url(r'^authorize/oauth2/', include(
        'holonet.apps.authorization.urls', namespace='oauth2_provider'
    )),
]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
