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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('prefix', models.CharField(validators=[holonet.mappings.validators.validate_local_part], unique=True, max_length=64, db_index=True)),
                ('tag', models.CharField(blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.EmailField(max_length=75)),
                ('tag', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='recipient_list',
            field=models.ManyToManyField(related_name='mailing_lists', blank=True, to='mappings.Recipient'),
            preserve_default=True,
        ),
    ]
