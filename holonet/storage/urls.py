from django.conf.urls import url

from .views import EmailStorageTypesView, EmailStorageView

urlpatterns = [
    url(r'^$', EmailStorageView.as_view(), name='list'),
    url(r'^types/$', EmailStorageTypesView.as_view(), name='types')
]
