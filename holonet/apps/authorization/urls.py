from django.conf.urls import include, url
from oauth2_provider import views as oauth2_views

oauth2_urlpatterns = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name='token'),
    url(r'^revoke_token/$', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
]

urlpatterns = [
    url(r'^oauth2/', include(oauth2_urlpatterns, namespace='oauth2_provider')),
]
