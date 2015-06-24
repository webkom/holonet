# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain',
            field=models.CharField(max_length=200, unique=True, db_index=True),
        ),
    ]
