# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.app.mappings.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20141113_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='member',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='prefix',
            field=models.CharField(verbose_name='prefix', max_length=64, unique=True, validators=[holonet.app.mappings.validators.validate_local_part]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=set([('mailing_list', 'address')]),
        ),
    ]
