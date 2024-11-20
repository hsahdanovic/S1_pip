def safe_lookup(d, keys, expected_type):
    try:
        for key in keys:
            d = d[key]
    except KeyError:
        return "Key not found"

    if not isinstance(d, expected_type):
        raise TypeError(f"Expected type {expected_type.__name__}, but got {type(d).__name__}")

    return d


if __name__ == "__main__":
    nested_dict = {"level1": {"level2": {"key": "value"}}}
    print(safe_lookup(nested_dict, ["level1", "level2", "key"], str))

    nested_dict = {"level1": {"level2": {"key": "value"}}}
    print(safe_lookup(nested_dict, ["level1", "wrong_key"], str))

    nested_dict = {"level1": {"level2": {"key": "value"}}}
    try:
        safe_lookup(nested_dict, ["level1", "level2"], list)
    except TypeError as e:
        print(e)