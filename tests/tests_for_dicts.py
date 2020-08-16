import pytest
from resources.dicts_test_data import *


@pytest.mark.parametrize(('dict_for_test', 'dict_for_update', 'expected'), data_for_update)
def test_update(dict_for_test, dict_for_update, expected):
    dict_upd = dict_for_test.copy()
    dict_for_upd = dict_for_update.copy()
    dict_upd.update(dict_for_upd)
    assert dict_upd == expected


@pytest.mark.parametrize(('dict_for_test', 'key', 'expected_value'), data_for_get)
def test_get(dict_for_test, key, expected_value):
    assert dict_for_test.get(key) == expected_value


@pytest.mark.parametrize(('dict_for_test', 'key', 'expected_dict'), data_for_pop)
def test_pop(dict_for_test, key, expected_dict):
    dict_pop = dict_for_test.copy()
    dict_pop.pop(key)
    assert dict_pop == expected_dict


@pytest.mark.parametrize(('dict_1', 'dict_2', 'expected_dict'), data_for_join)
def test_join(dict_1, dict_2, expected_dict):
    dic_join = {**dict_1, **dict_2}
    assert dic_join == expected_dict


@pytest.mark.parametrize(('dict_for_test', 'expected_dict'), data_for_invert)
def test_invert(dict_for_test, expected_dict):
    inv_dict = {v: k for k, v in dict_for_test.items()}
    assert inv_dict == expected_dict
