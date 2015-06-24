from django.conf import settings
from django.utils.timezone import now
from elasticsearch_dsl import F, Q, Date, DocType, String
from elasticsearch_dsl.connections import connections

from holonet.utils.types import assert_string

from . import StorageBackend, StoredEmail


class Backend(StorageBackend):

    @classmethod
    def configure(cls):
        connections.configure(**settings.ELASTICSEARCH)

    @classmethod
    def index_message(cls, message):
        super().index_message(message)

        mail = ElasticsearchEmailMapping(timestamp=message.timestamp, from_email=message.from_email,
                                         to=message.to, recipients=message.recipients,
                                         subject=message.subject, raw=message.raw,
                                         message_type=message.message_type)
        mail.save(index=cls.index_name(message.timestamp))

    @classmethod
    def retrieve_history(cls, from_time, to_time, filter=None, search_query=None):
        super().retrieve_history(from_time, to_time, filter, search_query)
        search = ElasticsearchEmailMapping.search()
        if filter is None:
            filter = StorageBackend.MESSAGE_TYPES

        time_filter = ((F('range', **{'timestamp': {'gt': from_time.isoformat()}}) &
                        F('range', **{'timestamp': {'lt': to_time.isoformat()}})))

        type_filter = (F('terms', message_type=filter))

        search = search.filter(time_filter)
        search = search.filter(type_filter)

        if search_query is not None and search_query != '':
            assert_string(search_query)
            freetext_query = Q("query_string", query=search_query)
            search = search.query(freetext_query)

        response = search.execute()

        return list(map(cls.model_to_stored_email, response))

    @classmethod
    def index_name(cls, timestamp=None):
        if timestamp is None:
            timestamp = now()
        time = timestamp.strftime(settings.ELASTICSEARCH_INDEX_PATTERN)
        index_name = 'holonet-%s' % time
        return index_name

    @classmethod
    def model_to_stored_email(cls, model_instance):
        return StoredEmail(model_instance.from_email, list(model_instance.to),
                           list(model_instance.recipients), model_instance.subject,
                           model_instance.raw, model_instance.message_type,
                           model_instance.timestamp)


class ElasticsearchEmailMapping(DocType):

    timestamp = Date()
    from_email = String(index='not_analyzed')
    to = String(fields={'raw': String(index='not_analyzed')})
    recipients = String(fields={'raw': String(index='not_analyzed')})
    subject = String()
    raw = String()
    message_type = String(index='not_analyzed')
