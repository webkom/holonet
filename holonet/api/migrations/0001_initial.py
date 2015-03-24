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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True, null=True)),
                ('valid_to', models.DateTimeField(null=True, blank=True)),
                ('application', models.ForeignKey(to='api.Application')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
