# -*- coding: utf8 -*-

from django.contrib import admin

from .models import DomainBlacklist, SenderBlacklist

admin.site.register(SenderBlacklist)
admin.site.register(DomainBlacklist)
