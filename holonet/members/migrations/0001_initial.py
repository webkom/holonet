# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=40)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=40)),
                ('email', models.EmailField(verbose_name='email address', max_length=254)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('acknowledge_posts', models.BooleanField(default=False)),
            ],
        ),
    ]
