from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('holonet.api.urls', namespace='api')),
    url(r'^authorize/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
