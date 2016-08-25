from rest_framework import routers

from holonet.apps.lists import views as list_views

router = routers.DefaultRouter()

router.register(r'domains', list_views.DomainViewSet)
router.register(r'lists', list_views.ListViewSet)
router.register(r'restricted_lists', list_views.RestrictedListViewSet)
router.register(r'list_members', list_views.ListMemberViewSet)
