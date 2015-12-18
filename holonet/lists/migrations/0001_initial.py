# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import basis.models
from django.db import migrations, models

import holonet.core.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('domain', holonet.core.fields.DomainField(max_length=254)),
                ('base_url', models.URLField()),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('list_name', holonet.core.fields.LocalPartField(max_length=254)),
                ('display_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True, help_text='Allow postings to this list.')),
                ('public', models.BooleanField(default=False, help_text='Allow non owners to post in this list.')),
                ('archive', models.BooleanField(default=False, help_text='Archive all messages to this list in the message storage.')),
                ('processed_messages', models.BigIntegerField(default=0)),
                ('emergency', models.BooleanField(default=False, help_text='Emergency held all messages for moderation by the list admin.')),
                ('require_explicit_destination', models.BooleanField(default=True, help_text='Catch messages with wrong destination. This is typically bcc messages.')),
                ('last_post_at', models.DateTimeField(blank=True, null=True, default=None)),
                ('member_posts', models.BooleanField(default=False, help_text='Only allow postings from list member addresses.')),
                ('nonmember_rejection_notice', models.TextField(default='You {list_name} list is a member-only list. Your message was rejected.')),
                ('include_rfc2369_headers', models.BooleanField(default=True)),
                ('anonymous_list', models.BooleanField(default=False, help_text='Remove sender address from postings to this list.')),
                ('subject_prefix', models.CharField(blank=True, max_length=100, help_text='Prefix subjects to this list.')),
                ('max_message_size', models.PositiveIntegerField(default=0, help_text='0 is unlimited.')),
                ('max_num_recipients', models.PositiveIntegerField(default=0, help_text='0 is unlimited.')),
                ('needs_manager_approval', models.BooleanField(default=False, help_text='All postages to this list needs approval in the admin panel')),
                ('use_verp', models.BooleanField(default=True)),
                ('verp_interval', models.PositiveIntegerField(default=10)),
                ('post_volume', models.PositiveIntegerField(default=0, help_text='0 is unlimited.')),
                ('post_volume_frequency', models.PositiveIntegerField(default=0, choices=[(0, 'yearly'), (1, 'monthly'), (2, 'daily'), (3, 'weekly'), (4, 'hourly'), (5, 'minutely')])),
                ('send_goodbye_message', models.BooleanField(default=False)),
                ('send_welcome_message', models.BooleanField(default=False)),
                ('process_bounces', models.BooleanField(default=True)),
                ('digestable', models.BooleanField(default=True)),
                ('digest_volume_frequency', models.PositiveIntegerField(default=3, choices=[(0, 'yearly'), (1, 'monthly'), (2, 'daily'), (3, 'weekly'), (4, 'hourly'), (5, 'minutely')])),
                ('digest_is_default', models.BooleanField(default=False)),
                ('digest_last_sent_at', models.DateTimeField(blank=True, null=True, default=None)),
                ('autorespond_postings', models.PositiveIntegerField(default=0, choices=[(0, 'continue'), (1, 'respond_and_continue'), (2, 'respond_and_discard')])),
                ('autoresponse_postings_text', models.TextField(default='You message to the list {list_name} is {action_name}.')),
                ('autorespond_requests', models.PositiveIntegerField(default=0, choices=[(0, 'continue'), (1, 'respond_and_continue'), (2, 'respond_and_discard')])),
                ('autoresponse_request_text', models.TextField(default='Your message to the list {list_name} has the status {action_name}.')),
                ('domain', models.ForeignKey(to='lists.Domain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
