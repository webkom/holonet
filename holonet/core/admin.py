# -*- coding: utf8 -*-

from django.contrib import admin

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist


@admin.register(SenderBlacklist)
class SenderBlacklistAdmin(admin.ModelAdmin):
    list_display = ('sender', )
    list_display_links = ('sender', )
    search_fields = ('sender', )
    ordering = ('sender',)


@admin.register(SenderWhitelist)
class SenderWhitelistAdmin(admin.ModelAdmin):
    list_display = ('sender', )
    list_display_links = ('sender', )
    search_fields = ('sender', )
    ordering = ('sender',)


@admin.register(DomainBlacklist)
class DomainBlacklistAdmin(admin.ModelAdmin):
    list_display = ('domain', )
    list_display_links = ('domain', )
    search_fields = ('domain', )
    ordering = ('domain',)


@admin.register(DomainWhitelist)
class DomainWhitelistAdmin(admin.ModelAdmin):
    list_display = ('domain', )
    list_display_links = ('domain', )
    search_fields = ('domain', )
    ordering = ('domain',)
