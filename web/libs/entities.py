from elasticsearch import Elasticsearch
from flask import current_app


def bulk(index_name, doc_type, bulk_list):
    """
    Bulk Create for Indices.
    """
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])

    bulk_data = []
    for row in bulk_list:
        op_dict = {
            "index": {
                "_index": index_name,
                "_type": doc_type,
                "_id": row['id']
            }
        }

        bulk_data.append(op_dict)
        bulk_data.append(row)

    es.bulk(bulk_data, index=index_name, doc_type=doc_type, refresh=True)


def remove(index_name, doc_type, object_id):
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])
    return es.delete(index=index_name,
                     id=object_id,
                     doc_type=doc_type,
                     ignore=[400, 404])


def get(index_name, doc_type, object_id, fields=None,
        exclude_fields=None):
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])
    body = {}

    if fields:
        body['_source_include'] = fields

    if exclude_fields:
        body['_source_exclude'] = exclude_fields

    response = es.get(index=index_name,
                      id=object_id,
                      doc_type=doc_type,
                      ignore=[400, 404],
                      **body)
    return response.get('_source', {})


def search(index_name, doc_type, query=None, order_by=None, offset=0, limit=15,
           fields=None, exclude_fields=None):
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])

    body = {}
    if query:
        body['query'] = query

    if order_by:
        body['sort'] = order_by

    body['_source'] = {
        'includes': ['*'],
        'excludes': []
    }

    if fields:
        body['_source']['includes'] = fields

    if exclude_fields:
        body['_source']['excludes'] = exclude_fields

    response = es.search(index=index_name,
                         doc_type=doc_type, body=body,
                         from_=offset, size=limit)

    hits = [
        dict(val['_source'].items())
        for val in response['hits']['hits']
    ]

    return {
        'total': int(response['hits']['total']), 'hits': hits
    }


def count(index_name, doc_type, query=None):
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])

    body = {}
    if query:
        body['query'] = query

    response = es.count(index=index_name, doc_type=doc_type, body=body)
    return response.get('count', 0)
