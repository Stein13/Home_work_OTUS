import pytest
from resources.strings_test_data import *


@pytest.mark.parametrize(('str_for_test', 'expected_str'), data_for_lowercase)
def test_change(str_for_test, expected_str):
    assert str_for_test.lower() == expected_str


@pytest.mark.parametrize(('str_for_test', 'expected_str'), data_for_uppercase)
def test_string_to_low_case(str_for_test, expected_str):
    assert str_for_test.upper() == expected_str


@pytest.mark.parametrize(('str_for_test', 'expected_str'), data_for_capitalize)
def test_string_capitalize(str_for_test, expected_str):
    assert str_for_test.capitalize() == expected_str


@pytest.mark.parametrize(('first_str', 'second_str', 'expected_str'), data_for_concatenation)
def test_string_concatenation(first_str, second_str, expected_str):
    result = first_str + second_string
    assert result == expected_str


@pytest.mark.parametrize(('string_for_test', 'string_len'), data_for_string_len)
def test_string_len(string_for_test, string_len):
    result = len(string_for_test)
    assert result == string_len
