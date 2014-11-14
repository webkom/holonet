# -*- coding: utf8 -*-

from elasticsearch import Elasticsearch

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
                    }
                }
            }
        )


def store_spam(message):
    index_check()
    connection = get_connection()
    connection.create(settings.INDEX_NAME, 'spam', message.index(), params={'_ttl': '52w'})
    return True
