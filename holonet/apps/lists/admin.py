from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Domain, List, ListMember, RestrictedList


class DomainAdmin(admin.ModelAdmin):
    model = Domain
    list_display = ['domain', 'base_url']
    search_fields = ('domain', 'base_url', 'description')
    ordering = ('domain', )

admin.site.register(Domain, DomainAdmin)


class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ['list_name', 'display_name', 'remote_identifier', 'active', 'last_post_at']

    list_filter = ('active', 'archive', 'member_posts', 'anonymous_list', 'use_verp')
    search_fields = ('list_name', 'display_name', 'description')
    ordering = ('list_name',)
    fieldsets = (
        (None, {'fields': ('list_name', 'display_name', 'remote_identifier', 'description',
                           'domains')}),
        (_('General'), {'fields': ('active', 'archive', 'include_rfc2369_headers',
                                   'anonymous_list', 'subject_prefix', 'max_message_size',
                                   'max_num_recipients', 'needs_manager_approval', 'emergency',
                                   'require_explicit_destination')}),
        (_('Meta'), {'fields': ('processed_messages', 'last_post_at')}),
        (_('Bounce'), {'fields': ('process_bounces', 'use_verp', 'verp_interval')}),
        (_('Members'), {'fields': ('members', )})
    )

admin.site.register(List, ListAdmin)


class RestrictedListAdmin(admin.ModelAdmin):
    model = RestrictedList
    list_display = ('token', 'from_address', 'timeout',)
    search_fields = ('token', 'from_address')
    ordering = ('-timeout',)
    fieldsets = (
        (None, {'fields': ('token', 'from_address', 'timeout')}),
        (_('Members'), {'fields': ('members', )})
    )

admin.site.register(RestrictedList, RestrictedListAdmin)


class ListMemberAdmin(admin.ModelAdmin):
    model = ListMember
    list_display = ('user', 'active')
    search_fields = ('user__username', 'user__email', )
    fieldsets = (
        (None, {'fields': ('user', 'active')}),
    )

admin.site.register(ListMember, ListMemberAdmin)
