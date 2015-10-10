from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('holonet.api.urls', namespace='api')),
    url(r'^authorize/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^$', login_required(TemplateView.as_view(template_name='frontend.html')),
        name='dashboard'),

    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]
