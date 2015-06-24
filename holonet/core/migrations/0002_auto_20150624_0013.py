# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senderblacklist',
            name='sender',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='senderwhitelist',
            name='sender',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
