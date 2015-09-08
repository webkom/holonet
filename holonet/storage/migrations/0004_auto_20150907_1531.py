# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20150824_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailstorage',
            name='message_type',
            field=models.CharField(choices=[('spam', 'spam'), ('blacklisted', 'blacklisted'), ('bounce', 'bounce'), ('archive', 'archive')], max_length=20),
        ),
    ]
