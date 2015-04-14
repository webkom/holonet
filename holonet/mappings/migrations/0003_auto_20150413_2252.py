# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20150413_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='tag',
            field=models.CharField(blank=True, unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='tag',
            field=models.CharField(blank=True, unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
