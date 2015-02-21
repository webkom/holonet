# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20150129_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='tag',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]