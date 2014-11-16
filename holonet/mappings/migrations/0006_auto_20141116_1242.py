# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0005_auto_20141116_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='recipient_list',
            field=models.ManyToManyField(blank=True, to='mappings.Recipient', verbose_name='recipients'),
            preserve_default=True,
        ),
    ]
