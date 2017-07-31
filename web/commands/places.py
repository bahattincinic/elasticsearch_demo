from flask_script import Manager
from flask import current_app

from libs.foursquare import FoursquareClient
from libs.indices import reload_elasticsearch_index
from libs.entities import bulk


manager = Manager(usage="Foursquare Places")


@manager.option('-l', '--point', dest='point', default='41.0082,28.9784')
def build(point):
    """
    Import places from Foursquare
    """
    index = current_app.config['ELASTICSEARCH_INDEX']
    with reload_elasticsearch_index(**index):
        client = FoursquareClient()
        places = client.venue_search({'ll': point, 'limit': 100})
        bulk([
            {
                'id': place['id'],
                'name': place['name'],
                'point': '%s,%s' % (place['location']['lng'], place['location']['lat']),
                'category': place['categories'][0]['name']
            }
            for place in places
        ])
