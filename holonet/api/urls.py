from django.conf.urls import include, url

from .views import BrowsableAPIView

urlpatterns = [
    url(r'^$', BrowsableAPIView.as_view(), name='browse'),
    url(r'^status/', include('holonet.status.urls', namespace='status')),
    url(r'^storage/', include('holonet.storage.urls', namespace='storage')),
]
