# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0005_restrictedmapping_recipient_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedmapping',
            name='tag',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
