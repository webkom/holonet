# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20150624_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailstorage',
            name='blind_copy',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AddField(
            model_name='emailstorage',
            name='copy',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.CharField(max_length=200), size=None),
        ),
    ]
