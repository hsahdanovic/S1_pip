def file_statistics(path: str, encoding: str = 'CP1252'):
    try:
        with open(path, 'r', encoding=encoding) as file:
            content = file.read()

        latins = 0
        digits = 0
        spaces = 0
        rest = []

        for char in content:
            if char.isalpha():
                latins += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                rest.append(char)

        return latins, digits, spaces, rest

    except Exception as e:
        raise ValueError(f"Error reading file '{path}': {e}")


if __name__ == "__main__":
    print(file_statistics('a7_ex3_cp1252.txt'))
    print(file_statistics('a7_ex3_utf8.txt',))
    print(file_statistics('a7_ex3_utf8.txt', encoding='utf-8'))