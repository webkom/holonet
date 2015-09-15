# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='processed_messages',
            field=models.BigIntegerField(default=0),
        ),
    ]
