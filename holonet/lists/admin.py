from django.contrib import admin

from .models import Domain, List


class DomainAdmin(admin.ModelAdmin):
    model = Domain
    list_display = ['domain', 'base_url']

admin.site.register(Domain, DomainAdmin)


class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ['list_name', 'display_name', 'active', 'last_post_at']

admin.site.register(List, ListAdmin)
