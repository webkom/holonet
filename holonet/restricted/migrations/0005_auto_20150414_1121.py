# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0004_auto_20150413_2253'),
    ]

    def restricted_change(apps, schema_editor):
        restricted_model = apps.get_model('restricted', 'RestrictedMapping')
        for restricted in restricted_model.objects.filter(tag=None):
            restricted.tag = restricted.pk
            restricted.save()

    operations = [
        migrations.RunPython(restricted_change),
        migrations.AlterField(
            model_name='restrictedmapping',
            name='tag',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
