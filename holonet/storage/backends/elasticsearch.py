from django.conf import settings
from django.utils.timezone import now
from elasticsearch_dsl import F, Q, Date, DocType, String
from elasticsearch_dsl.connections import connections

from holonet.storage.base import StorageBackend, StoredEmail


class Backend(StorageBackend):

    def configure(self):
        connections.configure(**settings.ELASTICSEARCH)

    def index_message(self, message):
        mail = ElasticsearchEmailMapping(**message.as_dict())
        mail.save(index=self.index_name(message.timestamp))

    def retrieve_history(self, from_time=None, to_time=None, filter=None, search_query=None):
        search = ElasticsearchEmailMapping.search()
        if filter is None:
            filter = StorageBackend.MESSAGE_TYPES_LIST

        type_filter = (F('terms', message_type=filter))
        search = search.filter(type_filter)

        if from_time is not None:
            from_time_filter = F('range', **{'timestamp': {'gt': from_time.isoformat()}})
            search = search.filter(from_time_filter)

        if to_time is not None:
            to_time_filter = F('range', **{'timestamp': {'lt': to_time.isoformat()}})
            search = search.filter(to_time_filter)

        if search_query is not None and search_query != '':
            freetext_query = Q("query_string", query=str(search_query))
            search = search.query(freetext_query)

        response = search.execute()

        return list(map(self.model_to_stored_email, response))

    def index_name(self, timestamp=None):
        if timestamp is None:
            timestamp = now()
        index_name = timestamp.strftime(settings.ELASTICSEARCH_INDEX_PATTERN)
        return index_name

    def model_to_stored_email(self, model_instance):
        return StoredEmail(**model_instance.as_dict())


class ElasticsearchEmailMapping(DocType):

    timestamp = Date()
    from_email = String(index='not_analyzed')
    to = String(fields={'raw': String(index='not_analyzed')})
    copy = String(fields={'raw': String(index='not_analyzed')})
    blind_copy = String(fields={'raw': String(index='not_analyzed')})
    recipients = String(fields={'raw': String(index='not_analyzed')})
    subject = String()
    raw = String()
    message_type = String(index='not_analyzed')

    def as_dict(self):
        return {
            'from_email': str(self.from_email),
            'to': list(self.to),
            'copy': list(self.copy),
            'blind_copy': list(self.blind_copy),
            'recipients': list(self.recipients),
            'subject': str(self.subject),
            'raw': str(self.raw),
            'message_type': str(self.message_type),
            'timestamp': self.timestamp
        }
