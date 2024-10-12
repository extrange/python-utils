def dict_diff[K, V](dict_1: dict[K, V], dict_2: dict[K, V]) -> dict[K, V]:
    """
    Return a dictionary of the k:v pairs from dict_2, which were different from dict_1.

    Will raise ValueError if keys in both dicts are not equal.

    Usage:

    ```python
    dict_1 = {"a": 2, "b": 1000}
    dict_2 = {"a": 2, "b": 3}
    assert dict_diff(dict_1, dict_2) == {"b": 3}
    ```

    """
    if dict_1.keys() != dict_2.keys():
        msg = "Dictionaries do not have the same set of keys"
        raise ValueError(msg)
    return {k: dict_2[k] for k in dict_1 if dict_1[k] != dict_2[k]}
