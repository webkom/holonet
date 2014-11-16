# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0002_auto_20141115_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('address', models.EmailField(max_length=75, verbose_name='address')),
                ('tag', models.CharField(unique=True, verbose_name='tag', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='member',
            name='mailing_list',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
