from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Member


class MemberModelAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'is_active')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Holonet'), {'fields': ('acknowledge_posts', )})
    )

admin.site.register(Member, MemberModelAdmin)
