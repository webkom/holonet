# -*- coding: utf8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from djcelery.models import CrontabSchedule, IntervalSchedule, PeriodicTask, TaskState, WorkerState

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist, User

admin.site.register(SenderBlacklist)
admin.site.register(DomainBlacklist)
admin.site.register(SenderWhitelist)
admin.site.register(DomainWhitelist)
admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)


class UserAdmin(AbstractUserAdmin):
    fieldsets = AbstractUserAdmin.fieldsets + (('SASL', {'fields': ('sasl_token',)}),)
admin.site.register(User, UserAdmin)
