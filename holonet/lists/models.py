from basis.models import TimeStampModel
from django.db import models
from django.utils.translation import ugettext_lazy as _

from holonet.core.defaults import DEFAULT_NONMEMBER_REJECTION_NOTICE
from holonet.core.fields import DomainField, LocalPartField


class Domain(TimeStampModel):

    domain = DomainField()
    base_url = models.URLField()
    description = models.TextField(blank=True)

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

    list_name = LocalPartField()
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    domain = models.ForeignKey(Domain)
    active = models.BooleanField(default=True, help_text='Allow postings to this list.')
    public = models.BooleanField(default=False, help_text=_('Allow non owners to post in this '
                                                            'list.'))
    archive = models.BooleanField(default=False, help_text='Archive all messages to this list in '
                                                           'the message storage.')
    processed_messages = models.BigIntegerField(default=0)
    emergency = models.BooleanField(default=False, help_text='Emergency held all messages for '
                                                             'moderation by the list admin.')
    require_explicit_destination = models.BooleanField(default=True,
                                                       help_text='Catch messages with wrong '
                                                                 'destination. This is typically '
                                                                 'bcc messages.')

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

    process_bounces = models.BooleanField(default=True)

    def __str__(self):
        return self.list_name

    @property
    def posting_address(self):
        """
        Construct the main address for this list. This is the primary address for this list.
        Aliases can be used to have multiple addresses mapped to this list.
        """
        return '{}@{}'.format(self.list_name, self.domain.domain)
