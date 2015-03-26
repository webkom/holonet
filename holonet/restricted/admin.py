# -*- coding: utf8 -*-

from django.contrib import admin

from .models import RestrictedMapping


class RestrictedInline(admin.TabularInline):
    model = RestrictedMapping.recipient_list.through
    extra = 1
    verbose_name = 'Restricted Mapping'


@admin.register(RestrictedMapping)
class RestrictedMappingAdmin(admin.ModelAdmin):
    list_display = ('from_address', 'token', 'valid_from', 'valid_to', 'tag', 'is_used')
    list_display_links = ('from_address', 'token')
    search_fields = ('from_address', 'token', 'tag')
    ordering = ('valid_to', 'is_used')

    fieldsets = (
        ('Restricted', {'fields': ('from_address', 'is_used', 'tag')}),
        ('Token', {'fields': ('token', 'valid_from', 'valid_to')}),
    )

    readonly_fields = ('token', )
    inlines = [RestrictedInline]
