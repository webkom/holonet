# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='recipient_list',
            field=models.ManyToManyField(to='mappings.Recipient', blank=True, related_name='mailing_lists'),
            preserve_default=True,
        ),
    ]
