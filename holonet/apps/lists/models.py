import uuid

from basis.models import TimeStampModel
from django.db import models

from holonet.apps.utils.fields import DomainField, LocalPartField

from .managers import RestrictedListManager


class Domain(TimeStampModel):

    remote_identifier = models.CharField(max_length=32, unique=True, db_index=True)
    domain = DomainField(unique=True)
    base_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
        if not self.base_url:
            self.base_url = 'http://{}'.format(self.domain)
        super().save(*args, **kwargs)


class ListMember(TimeStampModel):

    remote_identifier = models.CharField(max_length=32, unique=True, db_index=True)
    user = models.OneToOneField('authorization.User', null=True, blank=True,
                                related_name='list_member')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_email()

    def get_email(self):
        """
        Find the member email, prefer user if user is attached to the member.
        """
        if self.user and self.user.email:
            return self.user.email
        elif self.email:
            return self.email


class ListMemberMixin(models.Model):

    members = models.ManyToManyField(ListMember)

    class Meta:
        abstract = True


class List(TimeStampModel, ListMemberMixin):

    remote_identifier = models.CharField(max_length=32, unique=True, db_index=True)
    list_name = LocalPartField()
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    domains = models.ManyToManyField(Domain, blank=True)
    active = models.BooleanField(default=True, help_text='Allow postings to this list.')
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

    process_bounces = models.BooleanField(default=True)

    def __str__(self):
        return self.list_name

    def posting_addresses(self):
        """
        Generate a list of all possible addresses user can use to post messages to this list.
        """
        return ['{0}@{1}'.format(str(self), str(domain)) for domain in self.domains.all()]


class RestrictedList(TimeStampModel, ListMemberMixin):

    remote_identifier = models.CharField(max_length=32, unique=True, db_index=True)
    token = models.UUIDField(verbose_name='Token', default=uuid.uuid4, unique=True)
    from_address = models.EmailField(blank=True, verbose_name='From address')
    timeout = models.DateTimeField(verbose_name='Timeout')

    objects = RestrictedListManager()

    def __str__(self):
        return self.get_token()

    def get_token(self):
        return str(self.token)
