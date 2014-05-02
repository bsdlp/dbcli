import requests


class LeClient(object):
    def __init__(self):
        self.endpoint = 'http://dbios.herokuapp.com/'

    def request(self, path=None, params=None):
        self.path = path
        self.params = params
        result = None

        result = requests.get(self.endpoint + path, params=params)
        return result.json()
