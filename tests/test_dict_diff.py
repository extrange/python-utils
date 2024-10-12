import pytest

from python_utils.dict_diff import dict_diff


def test_identical_dict():
    dict_1 = {"a": 2, "b": 3}
    dict_2 = {"a": 2, "b": 3}
    assert dict_diff(dict_1, dict_2) == {}


def test_different_value_should_return_from_dict_2():
    dict_1 = {"a": 2, "b": 1000}
    dict_2 = {"a": 2, "b": 3}
    assert dict_diff(dict_1, dict_2) == {"b": 3}


def test_multiple_different_values():
    dict_1 = {"a": 2, "b": 1000, "c": "apple"}
    dict_2 = {"a": 2, "b": 3, "c": "tomato"}
    assert dict_diff(dict_1, dict_2) == {"b": 3, "c": "tomato"}


def test_raise_if_keys_different():
    dict_1 = {"a": 2, "b": "extra"}
    dict_2 = {"a": 2}
    with pytest.raises(ValueError, match="Dictionaries do not have"):
        dict_diff(dict_1, dict_2)
    with pytest.raises(ValueError, match="Dictionaries do not have"):
        dict_diff(dict_2, dict_1)
