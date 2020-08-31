import pytest
from resources.placeholder_test_data import *
from api_client.placeholder_json import PlaceholderJSON

api_client = PlaceholderJSON()


@pytest.mark.parametrize(('data', 'expected'), test_data_for_create_post)
def test_create_new_post(data, expected):
    response = api_client.post_new_resource(data)
    assert response['userId'] == expected


@pytest.mark.parametrize(('body', 'expected'), test_data_for_create_post)
def test_update_post(body, expected):
    response = api_client.update_resource(body, 1)
    assert response['userId'] == expected


def test_get_all_posts():
    response = api_client.get_list_all_resources()
    assert response is not False


def test_delete_post():
    response = api_client.delete_resource(1)
    assert response is True


def test_search_posts_by_user():
    response = api_client.search_resource('userId', 1)
    assert response is not False
