# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0004_auto_20150413_2253'),
    ]

    def recipient_change(apps, schema_editor):
        recipient_model = apps.get_model('mappings', 'Recipient')
        for recipient in recipient_model.objects.filter(tag=None):
            recipient.tag = recipient.pk
            recipient.save()

    def mapping_change(apps, schema_editor):
        mapping_model = apps.get_model('mappings', 'MailingList')
        for mapping in mapping_model.objects.filter(tag=None):
            mapping.tag = mapping.pk
            mapping.save()

    operations = [
        migrations.RunPython(recipient_change),
        migrations.RunPython(mapping_change),
        migrations.AlterField(
            model_name='mailinglist',
            name='tag',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='tag',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
