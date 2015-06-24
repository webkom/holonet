from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestrictedMapping',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=64, unique=True, default='')),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('from_address', models.EmailField(max_length=254)),
                ('is_used', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('recipient_list', models.ManyToManyField(related_name='restricted_lists', blank=True, to='lists.Recipient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
