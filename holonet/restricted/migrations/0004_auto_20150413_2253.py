# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0003_auto_20150413_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedmapping',
            name='tag',
            field=models.CharField(null=True, unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
