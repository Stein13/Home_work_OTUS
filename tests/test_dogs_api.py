import pytest
from resources.dogs_test_data import *
from api_client.dog_ceo import DogCeo
import re
api_client = DogCeo()


def test_get_all_breeds():
    response = api_client.get_all_sub_breeds()
    assert response['status'] == 'success'
    assert response['message'] == all_sub_breeds


@pytest.mark.parametrize('breed', all_breeds_list)
def test_get_by_breed_random_image(breed):
    response = api_client.get_random_image_by_breed(breed)
    assert response['status'] == 'success'
    img_link = response['message']
    result = re.match('%s%s' % (link_part, breed), img_link) is not None
    assert result == 1


@pytest.mark.parametrize('breed', all_breeds_list)
def test_get_by_breed_multiple_random_image(breed):
    response = api_client.get_multiple_image_by_breed(breed, 2)
    assert response['status'] == 'success'
    img_links = response['message']
    match_count = 0
    for i in img_links:
        if re.match('%s%s' % (link_part, breed), i) is not None:
            match_count += 1
    assert match_count == 2


def test_get_all_list():
    response = api_client.get_all_list()
    assert response['status'] == 'success'
    assert response['message'] == all_breeds_json


@pytest.mark.parametrize(('breed', 'expected_count'), data_for_all_images_by_breed)
def test_get_all_images_by_breed(breed, expected_count):
    response = api_client.get_all_images_by_breed(breed)
    assert response['status'] == 'success'
    img_links = response['message']
    match_count = 0
    for i in img_links:
        if re.match('%s%s' % (link_part, breed), i) is not None:
            match_count += 1
    assert match_count == expected_count
