# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0003_auto_20141116_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='recipients_list',
            field=models.ManyToManyField(verbose_name='recipients', to='mappings.Recipient'),
            preserve_default=True,
        ),
    ]
