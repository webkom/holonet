from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailStorage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('from_email', models.CharField(max_length=200)),
                ('to', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('subject', models.CharField(max_length=300)),
                ('raw', models.TextField()),
                ('type', models.CharField(max_length=20, choices=[('spam', 'spam'), ('blacklisted', 'blacklisted'), ('bounce', 'bounce')])),
            ],
        ),
    ]
