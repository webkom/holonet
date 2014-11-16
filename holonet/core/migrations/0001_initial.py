# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SenderBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sender', models.EmailField(unique=True, max_length=75, verbose_name='sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
