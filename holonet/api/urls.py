from django.conf.urls import include, url

from .router import router

urlpatterns = [
    url(r'^', include(router.urls)),
]
