from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'holonet.app.frontpage.views.frontpage'),
    url(r'^admin/', include(admin.site.urls)),
)
