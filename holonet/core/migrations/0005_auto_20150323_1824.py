# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sasl_password',
            field=models.CharField(max_length=40, blank=True, verbose_name='sasl password'),
            preserve_default=True,
        ),
    ]
