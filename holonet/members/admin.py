from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Member


class MemberModelAdmin(UserAdmin):
    model = Member
    fieldsets = UserAdmin.fieldsets + (
        (_('Preferences'), {'fields': ('acknowledge_posts', )}),
    )

admin.site.register(Member, MemberModelAdmin)
