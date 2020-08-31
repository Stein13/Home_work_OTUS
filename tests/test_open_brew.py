import pytest
from resources.open_brew_test_data import *
from api_client.openbrewer import OpenBrewer
api_client = OpenBrewer()


@pytest.mark.parametrize(('city', 'expected'), by_city_test_data)
def test_get_brew_by_city(city, expected):
    response = api_client.get_breweries_by_city(city)
    for i in response:
        assert i['city'] == expected


@pytest.mark.parametrize('brewery_type', by_type_test_data)
def test_get_by_type(brewery_type):
    response = api_client.get_breweries_by_type(brewery_type)
    for i in response:
        assert i['brewery_type'] == brewery_type


@pytest.mark.parametrize('per_page', ['12'])
def test_get_per_page(per_page):
    response = api_client.get_breweries_per_page(per_page)
    count = 0
    for i in response:
        count += 1
    assert count == 12


@pytest.mark.parametrize('brew_id', by_id_test_data)
def test_get_brew_by_id(brew_id):
    response = api_client.get_single_brewery(brew_id)
    assert response['id'] == brew_id


@pytest.mark.parametrize('query', query_test_data)
def test_search_brew(query):
    response = api_client.search_brewery(query)
    assert response[0]['name'] == query
