from api_client.http_service import HTTPService as API

resources = 'posts'


class PlaceholderJSON:
    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com/'

    def get_list_all_resources(self):
        response = API.get(self.url + resources)
        return response['data'] if response['is_successful'] else False

    def post_new_resource(self, body):
        response = API.post(self.url + resources, payload=body)
        return response['data'] if response['code'] == 201 else False

    def update_resource(self, body, post_id):
        response = API.put(self.url + resources + '/%s' % post_id, payload=body)
        return response['data'] if response['is_successful'] else False

    def delete_resource(self, post_id):
        response = API.delete(self.url + resources + '/%s' % post_id)
        return True if response['is_successful'] else False

    def search_resource(self, by, query):
        response = API.get(self.url + resources, params={by: query})
        return response['data'] if response['is_successful'] else False
