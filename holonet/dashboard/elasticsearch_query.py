# -*- coding: utf8 -*-

from holonet.core.elasticsearch import generate_interval, run_search


def graph_query(types, time_from, time_to, query=None):

    base_query = {
        "size": 500,
        "sort": {
            "@timestamp": "desc"
        },
        "aggregations": {

        },
        "query": {
            "filtered": {
                "filter": {
                    "bool": {
                        "must": [
                            {
                                "range": {
                                    "@timestamp": {
                                        "gte": time_from,
                                        "lte": time_to
                                    }
                                }
                            }
                        ],
                        "must_not": [

                        ],
                        "should": [
                        ]
                    }
                }
            }
        },
        "fields": [
            "*",
            "_source"
        ]
    }

    def add_aggregation(type):

        aggregation = {
            "name": type,
            "filter": {
                "type": {
                    "value": type
                }
            },
            "payload": {
                "filter": {
                    "type": {
                        "value": type
                    }
                },
                "aggs": {
                    "emails": {
                        "date_histogram": {
                            "field": "@timestamp",
                            "interval": generate_interval(time_to - time_from),
                            "min_doc_count": 0,
                            "extended_bounds": {
                                "min": time_from,
                                "max": time_to
                            }
                        }
                    }
                }
            }
        }

        return aggregation

    aggregations = map(add_aggregation, types)

    if query:
        base_query['query']['filtered']['query'] = {
            "match": {
                "source": query
            }
        }

    for aggregation in aggregations:
        base_query['aggregations'][aggregation['name']] = aggregation['payload']
        base_query['query']['filtered']['filter']['bool']['should'].append(aggregation['filter'])

    return run_search(base_query)
