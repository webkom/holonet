# -*- coding: utf8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import ConnectionError

from django.conf import settings


def get_connection():
    return Elasticsearch(settings.ELASTICSEARCH)


def generate_interval(timespan):
    delta = timespan / (1000 * 60 * 60)
    if delta <= 1:
        return '1m'
    elif delta <= 3:
        return '3m'
    elif delta <= 12:
        return '12m'
    elif delta <= 24:
        return '24m'
    elif delta <= 72:
        return '72m'
    elif delta <= 168:
        return '168m'
    elif delta <= 720:
        return '720m'
    elif delta <= 2160:
        return '2160m'
    else:
        return '1h'


def index_check():
    connection = get_connection()
    index_excist = connection.indices.exists(
        index=settings.INDEX_NAME
    )

    if not index_excist:
        connection.indices.create(
            index=settings.INDEX_NAME,
            body={
                "mappings": {
                    "spam": {
                        "_ttl": {
                            "enabled": True
                        },
                        "properties": {
                            "@timestamp": {
                                "type": "date"
                            }
                        }
                    },
                    "blacklisted": {
                        "_ttl": {
                            "enabled": True
                        },
                        "properties": {
                            "@timestamp": {
                                "type": "date"
                            }
                        }
                    },
                    "bounce": {
                        "_ttl": {
                            "enabled": True
                        },
                        "properties": {
                            "@timestamp": {
                                "type": "date"
                            }
                        }
                    }
                }
            }
        )


def store_message(message, type, ttl):
    try:
        index_check()
        connection = get_connection()
        connection.create(settings.INDEX_NAME, type, message.index(), params={'_ttl': ttl})
        return True
    except (ConnectionError, OSError):
        return False


def run_search(query, index=settings.INDEX_NAME, type=None):
    try:
        index_check()
        connection = get_connection()
        result = connection.search(index=index, doc_type=type, body=query)
        return result
    except (ConnectionError, OSError):
        return {}


def store_spam(message):
    store_message(message, 'spam', '52w')


def store_blacklisted_mail(message):
    store_message(message, 'blacklisted', '52w')


def store_bounce_mail(message):
    store_message(message, 'bounce', '52w')
