import pytest
from resources.sets_test_data import *


@pytest.mark.parametrize('set_for_test', set_for_testing)
@pytest.mark.parametrize('item', in_set)
def test_check_item_in_set(set_for_test, item):
    result = item in set_for_test
    assert result == 1


@pytest.mark.parametrize(('first_string', 'second_string', 'expected_set'), data_for_uniq_letters_in_set)
def test_uniq_letters_for_first_set(first_string, second_string, expected_set):
    first_set = set(first_string)
    second_set = set(second_string)
    result = first_set - second_set
    assert result == expected_set


@pytest.mark.parametrize(('first_set', 'second_set', 'expected_set'), data_for_all_letters_in_sets)
def test_all_letters_in_sets(first_set, second_set, expected_set):
    result = first_set | second_set
    assert result == expected_set


@pytest.mark.parametrize(('first_set', 'second_set', 'expected_set'), data_for_letters_in_both_sets)
def test_letters_in_both_sets(first_set, second_set, expected_set):
    result = first_set & second_set
    assert result == expected_set


@pytest.mark.parametrize(('first_set', 'second_set', 'expected_set'), data_for_letters_not_in_both_sets)
def test_letters_not_in_both_sets(first_set, second_set, expected_set):
    result = first_set ^ second_set
    assert result == expected_set
