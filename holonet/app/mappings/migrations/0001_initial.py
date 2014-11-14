# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.app.mappings.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('prefix', models.CharField(verbose_name='prefix', validators=[holonet.app.mappings.validators.validate_local_part], max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('member', models.EmailField(verbose_name='member', max_length=75)),
                ('mailing_list', models.ForeignKey(verbose_name='mailing list', to='mappings.MailingList', related_name='members')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
