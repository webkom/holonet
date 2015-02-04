# -*- coding: utf8 -*-

from django.contrib import admin

from .models import MailingList, Recipient

admin.site.register(MailingList)
admin.site.register(Recipient)
