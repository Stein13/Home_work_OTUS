import pytest

from resources.lists_test_data import *


@pytest.mark.parametrize(('list_for_test', 'appended_item', 'expected'), data_for_append)
def test_append(list_for_test, appended_item, expected):
    list_app = list_for_test.copy()
    list_app.append(appended_item)
    assert list_app == expected


@pytest.mark.parametrize(('list_for_test', 'list_for_ex', 'expected'), data_for_extend)
def test_extend(list_for_test, list_for_ex, expected):
    list_ex = list_for_test.copy()
    list_ex.extend(list_for_ex)
    assert list_ex == expected


@pytest.mark.parametrize(('list_for_test', 'position', 'item_for_insert', 'expected'), data_for_insert)
def test_insert(list_for_test, position, item_for_insert, expected):
    list_ins = list_for_test.copy()
    list_ins.insert(position, item_for_insert)
    assert list_ins == expected


@pytest.mark.parametrize(('list_for_test', 'item_for_remove', 'expected'), data_for_remove)
def test_remove(list_for_test, item_for_remove, expected):
    list_rm = list_for_test.copy()
    list_rm.remove(item_for_remove)
    assert list_rm == expected


@pytest.mark.parametrize(('list_for_test', 'expected'), data_for_reverse)
def test_reverse(list_for_test, expected):
    list_rev = list_for_test.copy()
    list_rev.reverse()
    assert list_rev == expected
