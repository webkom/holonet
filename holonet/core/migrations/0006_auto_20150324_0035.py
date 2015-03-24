# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150323_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sasl_password',
        ),
        migrations.AddField(
            model_name='user',
            name='sasl_token',
            field=models.CharField(max_length=32, unique=True, verbose_name='sasl password', default='INVALID'),
            preserve_default=False,
        ),
    ]
