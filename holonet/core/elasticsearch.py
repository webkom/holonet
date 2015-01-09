# -*- coding: utf8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import ConnectionError

from django.conf import settings


def get_connection():
    return Elasticsearch(settings.ELASTICSEARCH)


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
                        }
                    },
                    "blacklisted": {
                        "_ttl": {
                            "enabled": True
                        }
                    },
                    "bounce": {
                        "_ttl": {
                            "enabled": True
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
    except ConnectionError:
        return False
    except OSError:
        return False


def store_spam(message):
    store_message(message, 'spam', '52w')


def store_blacklisted_mail(message):
    store_message(message, 'blacklisted', '52w')


def store_bounce_mail(message):
    store_message(message, 'bounce', '52w')
