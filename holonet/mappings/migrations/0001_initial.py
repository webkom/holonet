# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import holonet.mappings.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('prefix', models.CharField(verbose_name='prefix', validators=[holonet.mappings.validators.validate_local_part], unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('address', models.EmailField(verbose_name='address', max_length=75)),
                ('mailing_list', models.ForeignKey(related_name='members', verbose_name='mailing list', to='mappings.MailingList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=set([('mailing_list', 'address')]),
        ),
    ]
