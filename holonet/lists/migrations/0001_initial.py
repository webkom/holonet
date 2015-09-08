# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import basis.models
from django.db import migrations, models

import holonet.common.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('domain', holonet.common.fields.DomainField(max_length=254)),
                ('base_url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('list_name', holonet.common.fields.LocalPartField(max_length=254)),
                ('display_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(help_text='Allow postings to this list.', default=True)),
                ('archive', models.BooleanField(help_text='Archive all messages to this list in the message storage.', default=False)),
                ('last_post_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('member_posts', models.BooleanField(help_text='Only allow postings from list member addresses.', default=False)),
                ('nonmember_rejection_notice', models.TextField(default='You {list_name} list is a member-only list. Your message was rejected.')),
                ('include_rfc2369_headers', models.BooleanField(default=True)),
                ('anonymous_list', models.BooleanField(help_text='Remove sender address from postings to this list.', default=False)),
                ('subject_prefix', models.CharField(help_text='Prefix subjects to this list.', max_length=100, blank=True)),
                ('max_message_size', models.PositiveIntegerField(help_text='0 is unlimited.', default=0)),
                ('max_num_recipients', models.PositiveIntegerField(help_text='0 is unlimited.', default=0)),
                ('needs_manager_approval', models.BooleanField(help_text='All postages to this list needs approval in the admin panel', default=False)),
                ('use_verp', models.BooleanField(default=True)),
                ('verp_interval', models.PositiveIntegerField(default=10)),
                ('post_volume', models.PositiveIntegerField(help_text='0 is unlimited.', default=0)),
                ('post_volume_frequency', models.PositiveIntegerField(choices=[(0, 'yearly'), (1, 'monthly'), (2, 'daily'), (3, 'weekly'), (4, 'hourly'), (5, 'minutely')], default=0)),
                ('send_goodbye_message', models.BooleanField(default=False)),
                ('send_welcome_message', models.BooleanField(default=False)),
                ('process_bounces', models.BooleanField(default=True)),
                ('digestable', models.BooleanField(default=True)),
                ('digest_volume_frequency', models.PositiveIntegerField(choices=[(0, 'yearly'), (1, 'monthly'), (2, 'daily'), (3, 'weekly'), (4, 'hourly'), (5, 'minutely')], default=3)),
                ('digest_is_default', models.BooleanField(default=False)),
                ('digest_last_sent_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('autorespond_postings', models.PositiveIntegerField(choices=[(0, 'continue'), (1, 'respond_and_continue'), (2, 'respond_and_discard')], default=0)),
                ('autoresponse_postings_text', models.TextField(default='You message to the list {list_name} is {action_name}.')),
                ('autorespond_requests', models.PositiveIntegerField(choices=[(0, 'continue'), (1, 'respond_and_continue'), (2, 'respond_and_discard')], default=0)),
                ('autoresponse_request_text', models.TextField(default='Your message to the list {list_name} has the status {action_name}.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
