# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='acknowledge_posts',
            field=models.BooleanField(default=False, help_text='When this member posts to a list, receive a acknowledgement.'),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=128, blank=True, verbose_name='password'),
        ),
    ]
