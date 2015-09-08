from django.conf.urls import url

from .views import StatusTypesView, StatusView

urlpatterns = [
    url(r'^$', StatusView.as_view(), name='list'),
    url(r'^types/$', StatusTypesView.as_view(), name='types')
]
