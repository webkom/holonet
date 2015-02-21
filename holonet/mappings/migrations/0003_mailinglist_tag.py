# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20150129_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='tag',
            field=models.CharField(blank=True, validators=[holonet.core.validators.unique_or_blank], max_length=100),
            preserve_default=True,
        ),
    ]
