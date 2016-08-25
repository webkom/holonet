from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(AbstractUserAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
