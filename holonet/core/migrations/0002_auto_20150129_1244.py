# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainblacklist',
            name='domain',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
