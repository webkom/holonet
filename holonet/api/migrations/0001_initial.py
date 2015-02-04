# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('token', models.CharField(unique=True, max_length=64)),
                ('valid_from', models.DateTimeField(auto_now_add=True, null=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(to='api.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
