from flask_script import Manager
from flask import current_app

from libs.foursquare import FoursquareClient
from libs.indices import reload_elasticsearch_index
from libs.entities import bulk


manager = Manager(usage="Foursquare Places")


@manager.option('-l', '--point', dest='point', default='41.0082,28.9784')
def build(point):
    """
    Reload Elasticsearch & Import places from Foursquare
    """
    index = current_app.config['ELASTICSEARCH_INDEX']
    with reload_elasticsearch_index(**index):
        client = FoursquareClient()
        places = client.venue_search({'ll': point, 'limit': 100})
        bulk(
            index_name=index['index_name'],
            doc_type=index['doc_type'],
            bulk_list=client.normalize_places(places)
        )


@manager.option('-l', '--point', dest='point', default='41.0082,28.9784')
def load(point):
    """
    Import more places without elasticsearch reload
    """
    client = FoursquareClient()
    places = client.venue_search({'ll': point, 'limit': 100})
    bulk(client.normalize_places(places))
