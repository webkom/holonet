# -*- coding: utf8 -*-

from django.contrib import admin

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist

admin.site.register(SenderBlacklist)
admin.site.register(DomainBlacklist)
admin.site.register(SenderWhitelist)
admin.site.register(DomainWhitelist)
