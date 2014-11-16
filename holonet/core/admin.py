# -*- coding: utf8 -*-

from django.contrib import admin

from .models import SenderBlacklist, DomainBlacklist


admin.site.register(SenderBlacklist)
admin.site.register(DomainBlacklist)
