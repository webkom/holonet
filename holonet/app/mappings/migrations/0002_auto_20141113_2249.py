# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('member', models.EmailField(max_length=75, verbose_name='member')),
                ('mailing_list', models.ForeignKey(to='mappings.MailingList', related_name='members', verbose_name='mailing list')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='members',
            name='mailing_list',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
