# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import holonet.mappings.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('prefix', models.CharField(max_length=64, validators=[holonet.mappings.validators.validate_local_part], db_index=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('address', models.EmailField(max_length=75)),
                ('tag', models.CharField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='recipient_list',
            field=models.ManyToManyField(blank=True, to='mappings.Recipient'),
            preserve_default=True,
        ),
    ]
