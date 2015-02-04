# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20150129_1244'),
        ('restricted', '0004_auto_20150202_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedmapping',
            name='recipient_list',
            field=models.ManyToManyField(blank=True, related_name='restricted_lists', to='mappings.Recipient'),
            preserve_default=True,
        ),
    ]
