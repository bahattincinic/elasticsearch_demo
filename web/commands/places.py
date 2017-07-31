from flask_script import Manager

from libs.foursquare import FoursquareClient


manager = Manager(usage="Foursquare Places")


@manager.option('-l', '--point', dest='point', default='41.0082,28.9784')
def load(point):
    """
    Import places from Foursquare
    """
    client = FoursquareClient()
    response = client.venue_search({
        'll': point,
        'limit': 100
    })
    print(response)
