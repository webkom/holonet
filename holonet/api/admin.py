# -*- coding: utf8 -*-

from django.contrib import admin

from .models import Application, Token


class TokenInline(admin.TabularInline):
    model = Token
    fieldsets = (
        ('Token', {'fields': ('token',)}),
        ('Valid', {'fields': ('valid_to', 'valid_from')}),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [TokenInline]
    search_fields = ('name', )
    ordering = ('name',)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('application', 'token', 'valid_from', 'valid_to')
    list_display_links = ('application', 'token')
    search_fields = ('application', )
    ordering = ('application',)
    readonly_fields = ('token', )
    fields = ('token', 'application', 'valid_from', 'valid_to')
