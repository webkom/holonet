# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('token', models.CharField(max_length=64, unique=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True, null=True, verbose_name='valid from')),
                ('valid_to', models.DateTimeField(blank=True, verbose_name='valid to', null=True)),
                ('application', models.ForeignKey(to='api.Application', verbose_name='application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
