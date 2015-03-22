# -*- coding: utf8 -*-

from django.contrib import admin
from djcelery.models import CrontabSchedule, IntervalSchedule, PeriodicTask, TaskState, WorkerState

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist

admin.site.register(SenderBlacklist)
admin.site.register(DomainBlacklist)
admin.site.register(SenderWhitelist)
admin.site.register(DomainWhitelist)
admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)
