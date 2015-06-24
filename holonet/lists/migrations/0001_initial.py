from __future__ import unicode_literals

from django.db import migrations, models

import holonet.lists.validators


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0002_auto_20150525_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('prefix', models.CharField(max_length=64, validators=[holonet.lists.validators.validate_local_part], unique=True, db_index=True)),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('domain', models.ForeignKey(related_name='lists', to='domains.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('address', models.EmailField(max_length=254)),
                ('tag', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='recipient_list',
            field=models.ManyToManyField(to='lists.Recipient', blank=True, related_name='mailing_lists'),
        ),
    ]
