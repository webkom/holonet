# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0005_restrictedmapping_recipient_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedmapping',
            name='tag',
            field=models.CharField(blank=True, validators=[holonet.core.validators.unique_or_blank], max_length=100),
            preserve_default=True,
        ),
    ]
