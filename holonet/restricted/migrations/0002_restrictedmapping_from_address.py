# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedmapping',
            name='from_address',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
