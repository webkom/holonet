# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedmapping',
            name='tag',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
    ]
