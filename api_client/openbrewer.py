from api_client.http_service import HTTPService as API


class OpenBrewer:
    def __init__(self):
        self.url = 'https://api.openbrewerydb.org/breweries'

    # Endpoints
    def get_breweries(self):
        response = API.get(self.url)
        return response['data'] if response['is_successful'] else False

    def get_breweries_by_city(self, city):
        response = API.get(self.url, params={'by_city': city})
        return response['data'] if response['is_successful'] else False

    def get_breweries_by_name(self, name):
        response = API.get(self.url, params={'by_name': name})
        return response['data'] if response['is_successful'] else False

    def get_breweries_by_state(self, state):
        response = API.get(self.url, params={'by_state': state})
        return response['data'] if response['is_successful'] else False

    def get_breweries_by_postal(self, postal_code):
        response = API.get(self.url, params={'by_postal': postal_code})
        return response['data'] if response['is_successful'] else False

    def get_breweries_by_type(self, brew_type):
        response = API.get(self.url, params={'by_type': brew_type})
        return response['data'] if response['is_successful'] else False

    def get_breweries_page(self, page_number):
        response = API.get(self.url, params={'page': page_number})
        return response['data'] if response['is_successful'] else False

    def get_breweries_per_page(self, pages_count):
        response = API.get(self.url, params={'per_page': pages_count})
        return response['data'] if response['is_successful'] else False

    def get_single_brewery(self, brewery_id):
        response = API.get(self.url + "/%s" % brewery_id)
        return response['data'] if response['is_successful'] else False

    def search_brewery(self, query):
        response = API.get(self.url + '/search', params={'query': query})
        return response['data'] if response['is_successful'] else False
