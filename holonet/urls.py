from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'holonet.dashboad.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'holonet.dashboad.views.index'}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('holonet.api.urls'))
)
