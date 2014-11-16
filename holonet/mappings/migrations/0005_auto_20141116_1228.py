# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0004_mailinglist_recipients_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglist',
            old_name='recipients_list',
            new_name='recipient_list',
        ),
    ]
