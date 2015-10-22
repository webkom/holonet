# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list_processed_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='public',
            field=models.BooleanField(default=False, help_text='Allow non owners to post in this list.'),
        ),
    ]
