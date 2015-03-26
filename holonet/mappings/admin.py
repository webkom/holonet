# -*- coding: utf8 -*-

from django.contrib import admin

from holonet.restricted.admin import RestrictedInline

from .models import MailingList, Recipient


class MailingListInline(admin.TabularInline):
    model = MailingList.recipient_list.through
    extra = 1


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('address', 'tag')
    list_display_links = ('address', 'tag')
    search_fields = ('address', 'tag')
    ordering = ('address', )
    inlines = [MailingListInline, RestrictedInline]


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'tag')
    list_display_links = ('prefix', 'tag')
    search_fields = ('prefix', 'tag')
    ordering = ('prefix', )
    inlines = [MailingListInline]
