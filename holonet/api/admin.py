# -*- coding: utf8 -*-

from django.contrib import admin

from .models import Application, Token

admin.site.register(Application)
admin.site.register(Token)
