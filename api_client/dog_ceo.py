from api_client.http_service import HTTPService as API


class DogCeo:
    def __init__(self):
        self.url = 'https://dog.ceo/api/'

    # Endpoints
    def get_all_sub_breeds(self):
        response = API.get(self.url + 'breed/hound/list')
        return response['data'] if response['is_successful'] else False

    def get_random_image_by_breed(self, breed):
        response = API.get(self.url + 'breed/%s' % breed + '/images/random')
        return response['data'] if response['is_successful'] else False

    def get_all_list(self):
        response = API.get(self.url + 'breeds/list/all')
        return response['data'] if response['is_successful'] else False

    def get_multiple_image_by_breed(self, breed, number):
        response = API.get(self.url + 'breed/%s' % breed + '/images/random/%s' % number)
        return response['data'] if response['is_successful'] else False

    def get_all_images_by_breed(self, breed):
        response = API.get(self.url + 'breed/%s' % breed + '/images')
        return response['data'] if response['is_successful'] else False