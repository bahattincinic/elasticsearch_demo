from contextlib import contextmanager

from elasticsearch import Elasticsearch
from flask import current_app


def delete_indice(es, index_name):
    """
    Delete an index in Elasticsearch
    """
    es.indices.delete(index=index_name, ignore=[400, 404])


def create_indice(es, index_name, doc_type, mapping):
    """
    Create an index in Elasticsearch
    """

    body = {doc_type: mapping}

    index_settings = {
        'settings': {
            'number_of_shards': current_app.config['ELASTICSEARCH_NUMBER_OF_SHARDS'],
            'number_of_replicas': current_app.config['ELASTICSEARCH_NUMBER_OF_REPLICAS']
        }
    }

    es.indices.create(index=index_name, body=index_settings)
    es.indices.put_mapping(index=index_name,
                           doc_type=doc_type,
                           body=body)


def refresh(es):
    """
    Refresh elasticsearch Indices
    """
    es.indices.refresh()


@contextmanager
def reload_elasticsearch_index(index_name, doc_type, mapping):
    """
    This context manager does one than more process.
    - Delete existing index.
    - Create index.
    - Refresh index.
    """
    es = Elasticsearch(current_app.config['ELASTICSEARCH_URL'])

    # delete old index first
    delete_indice(es, index_name)
    # create new index from scratch
    create_indice(es, index_name, doc_type, mapping)
    yield index_name
    # refresh
    refresh(es)
