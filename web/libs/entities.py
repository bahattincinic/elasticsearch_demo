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
