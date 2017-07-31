import requests

from flask import current_app


class FoursquareClient(object):
    base_url = 'https://api.foursquare.com/v2/'
    version = '20161016'
    urls = {
        'venue': 'venues/search'
    }

    def __init__(self):
        self.client_id = current_app.config['FOURSQUARE_CLIENT_ID']
        self.client_secret = current_app.config['FOURSQUARE_CLIENT_SECRET']

    def _make_request(self, method, endpoint, params):
        api_call_params = params or {}
        api_call_params.update({
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'v': self.version
        })

        resp = requests.request(url=self.base_url + endpoint,
                                method=method,
                                params=api_call_params)
        resp.raise_for_status()
        return resp.json()

    def venue_search(self, params):
        response = self._make_request(endpoint=self.urls['venue'],
                                      method='GET', params=params)
        return response['response']['venues']
