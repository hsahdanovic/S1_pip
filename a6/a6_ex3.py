def flatten_dict(d: dict, parent: str = '', sep: str = '.') -> dict:
    flat = {}
    for key, value in d.items():
        new = f"{parent}{sep}{key}" if parent else key
        if isinstance(value, dict):
            flat.update(flatten_dict(value, new, sep=sep))
        else:
            flat[new] = value
    return flat

if __name__ == '__main__':
    print(f"result: {flatten_dict({})}")
    print(f"result: {flatten_dict({'a': 1, 'b': 2})}")
    print(f"result: {flatten_dict({'a': 1, 'b': 2, 'c.a': 3, 'c.b.a': 4, 'c.b.b': 5, 'd': 6})}")