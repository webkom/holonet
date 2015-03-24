# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestrictedMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('token', models.CharField(max_length=64, unique=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True, null=True)),
                ('valid_to', models.DateTimeField(null=True, blank=True)),
                ('from_address', models.EmailField(max_length=75)),
                ('is_used', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=100, blank=True)),
                ('recipient_list', models.ManyToManyField(related_name='restricted_lists', to='mappings.Recipient', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
