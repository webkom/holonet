from basis.models import TimeStampModel
from django.db import models

from holonet.core.defaults import (DEFAULT_AUTORESPONSE_POSTINGS_TEXT,
                                   DEFAULT_AUTORESPONSE_REQUEST_TEXT,
                                   DEFAULT_NONMEMBER_REJECTION_NOTICE)
from holonet.core.fields import DomainField, LocalPartField


class Domain(TimeStampModel):

    domain = DomainField()
    base_url = models.URLField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.base_url:
            self.base_url = 'http://{}'.format(self.domain)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.domain


class List(TimeStampModel):

    POST_FREQUENCY = (
        (0, 'yearly'),
        (1, 'monthly'),
        (2, 'daily'),
        (3, 'weekly'),
        (4, 'hourly'),
        (5, 'minutely'),
    )

    AUTORESPOND_ACTION = (
        (0, 'continue'),
        (1, 'respond_and_continue'),
        (2, 'respond_and_discard'),
    )

    list_name = LocalPartField()
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True, help_text='Allow postings to this list.')
    public = models.BooleanField(default=False)
    archive = models.BooleanField(default=False, help_text='Archive all messages to this list in '
                                                           'the message storage.')
    processed_messages = models.BigIntegerField(default=0)

    last_post_at = models.DateTimeField(null=True, default=None, blank=True)

    member_posts = models.BooleanField(default=False, help_text='Only allow postings from list '
                                                                'member addresses.')
    nonmember_rejection_notice = models.TextField(default=DEFAULT_NONMEMBER_REJECTION_NOTICE)

    include_rfc2369_headers = models.BooleanField(default=True)
    anonymous_list = models.BooleanField(default=False, help_text='Remove sender address from '
                                                                  'postings to this list.')
    subject_prefix = models.CharField(blank=True, max_length=100, help_text='Prefix subjects to '
                                                                            'this list.')
    max_message_size = models.PositiveIntegerField(default=0, help_text='0 is unlimited.')
    max_num_recipients = models.PositiveIntegerField(default=0, help_text='0 is unlimited.')
    needs_manager_approval = models.BooleanField(default=False, help_text='All postages to this '
                                                                          'list needs approval in '
                                                                          'the admin panel')

    use_verp = models.BooleanField(default=True)
    verp_interval = models.PositiveIntegerField(default=10)

    post_volume = models.PositiveIntegerField(default=0, help_text='0 is unlimited.')
    post_volume_frequency = models.PositiveIntegerField(choices=POST_FREQUENCY, default=0)

    send_goodbye_message = models.BooleanField(default=False)
    send_welcome_message = models.BooleanField(default=False)

    process_bounces = models.BooleanField(default=True)

    digestable = models.BooleanField(default=True)
    digest_volume_frequency = models.PositiveIntegerField(choices=POST_FREQUENCY, default=3)
    digest_is_default = models.BooleanField(default=False)
    digest_last_sent_at = models.DateTimeField(null=True, default=None, blank=True)

    autorespond_postings = models.PositiveIntegerField(choices=AUTORESPOND_ACTION, default=0)
    autoresponse_postings_text = models.TextField(default=DEFAULT_AUTORESPONSE_POSTINGS_TEXT)
    autorespond_requests = models.PositiveIntegerField(choices=AUTORESPOND_ACTION, default=0)
    autoresponse_request_text = models.TextField(default=DEFAULT_AUTORESPONSE_REQUEST_TEXT)
