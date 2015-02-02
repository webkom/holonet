# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0002_restrictedmapping_from_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedmapping',
            name='is_used',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
