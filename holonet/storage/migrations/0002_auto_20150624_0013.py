# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailstorage',
            old_name='type',
            new_name='message_type',
        ),
    ]
