# -*- coding: utf8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required()
def index(request):
    if request.user.is_staff:
        return render(request, 'dashboard/index.html')
    else:
        return redirect('holonet.dashboard.views.profile')


@login_required()
def profile(request):
    return render(request, 'dashboard/profile.html', {
        'system_name': settings.SYSTEM_NAME,
        'system_owner': settings.SYSTEM_OWNER,
        'smtp_server': settings.SMTP_SERVER,
        'smtp_port': settings.SMTP_PORT,
        'smtp_encryption_method': settings.SMTP_ENCRYPTION_METHOD,
        'smtp_authentication_method': settings.SMTP_AUTHENTICATION_METHOD,
        'domains': settings.MASTER_DOMAINS,
        'support': settings.SYSTEM_SUPPORT
    })
