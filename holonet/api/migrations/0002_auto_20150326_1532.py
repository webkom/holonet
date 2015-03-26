# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='application',
            field=models.ForeignKey(to='api.Application', related_name='tokens'),
            preserve_default=True,
        ),
    ]
