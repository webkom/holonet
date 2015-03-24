from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'holonet.dashboard.views.index'),
    url(r'^profile/$', 'holonet.dashboard.views.profile'),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'holonet.dashboard.views.index'}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('holonet.api.urls'))
]
