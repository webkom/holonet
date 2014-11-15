# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.mappings.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='prefix',
            field=models.CharField(unique=True, validators=[holonet.mappings.validators.validate_local_part], verbose_name='prefix', db_index=True, max_length=64),
            preserve_default=True,
        ),
    ]
