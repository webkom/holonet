# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0003_restrictedmapping_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedmapping',
            name='from_address',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restrictedmapping',
            name='is_used',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
