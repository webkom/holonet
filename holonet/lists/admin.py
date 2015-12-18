from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Domain, List


class DomainAdmin(admin.ModelAdmin):
    model = Domain
    list_display = ['domain', 'base_url']
    search_fields = ('domain', 'base_url', 'description')
    ordering = ('domain', )

admin.site.register(Domain, DomainAdmin)


class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ['posting_address', 'display_name', 'active', 'last_post_at']

    list_filter = ('active', 'public', 'archive', 'member_posts', 'anonymous_list', 'use_verp',
                   'digestable')
    search_fields = ('list_name', 'display_name', 'description', 'domain__domain')
    ordering = ('list_name',)
    fieldsets = (
        (None, {'fields': ('list_name', 'display_name', 'description', 'domain')}),
        (_('General'), {'fields': ('active', 'public', 'archive', 'include_rfc2369_headers',
                                   'anonymous_list', 'subject_prefix', 'max_message_size',
                                   'max_num_recipients', 'needs_manager_approval', 'emergency',
                                   'require_explicit_destination')}),
        (_('Meta'), {'fields': ('processed_messages', 'last_post_at')}),
        (_('Rejections'), {'fields': ('member_posts', 'nonmember_rejection_notice')}),
        (_('Bounce'), {'fields': ('process_bounces', 'use_verp', 'verp_interval')}),
        (_('Post Volume'), {'fields': ('post_volume', 'post_volume_frequency')}),
        (_('Messages'), {'fields': ('send_goodbye_message', 'send_welcome_message')}),
        (_('Digest'), {'fields': ('digestable', 'digest_volume_frequency', 'digest_is_default',
                                  'digest_last_sent_at')}),
        (_('Auto responses'), {'fields': ('autorespond_postings', 'autoresponse_postings_text',
                                          'autorespond_requests', 'autoresponse_request_text')}),
    )

admin.site.register(List, ListAdmin)
