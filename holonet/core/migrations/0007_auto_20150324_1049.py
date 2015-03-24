# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150324_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sasl_token',
            field=models.CharField(max_length=32, verbose_name='SASL Token', unique=True),
            preserve_default=True,
        ),
    ]
