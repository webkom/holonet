# -*- coding: utf8 -*-

from django.contrib import admin
from djcelery.models import CrontabSchedule, IntervalSchedule, PeriodicTask, TaskState, WorkerState

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist

admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)


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
