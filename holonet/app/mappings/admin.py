# -*- coding: utf8 -*-

from django.contrib import admin

from .models import MailingList, Member


admin.site.register(MailingList)
admin.site.register(Member)
