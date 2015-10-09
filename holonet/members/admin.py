from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Member


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'


class UserMemberAdmin(UserAdmin):
    inlines = (MemberInline, )


admin.site.unregister(User)
admin.site.register(User, UserMemberAdmin)
