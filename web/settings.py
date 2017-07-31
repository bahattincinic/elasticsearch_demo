class Config(object):
    DEBUG = False
    FOURSQUARE_CLIENT_ID = 'HD2ROBTRKGWOSTUS4MCEMTNFT5CO4MCXR0GRXA0STXAQJRU5'
    FOURSQUARE_CLIENT_SECRET = 'OCXEGH4HK4XDPM0SAKSXQJBWJYRNMF5KF55KOH4KUPPP224J'
    ELASTICSEARCH_URL = '127.0.0.1:9200'
    ELASTICSEARCH_NUMBER_OF_SHARDS = 5
    PER_PAGE = 25
    ELASTICSEARCH_NUMBER_OF_REPLICAS = 1
    ELASTICSEARCH_INDEX = {
        'index_name': 'places',
        'doc_type': 'places',
        'mapping': {
            'properties': {
                'title': {
                    'type': 'string',
                    'index' : 'not_analyzed'
                },
                'point': {
                    'type': 'geo_point'
                },
                'category': {
                    'type': 'string',
                    'index' : 'not_analyzed'
                }
            }
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True
