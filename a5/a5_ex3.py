def safe_list_access(lst, index):
    try:
        if not isinstance(lst, list):
            return "First argument is not a list"

        if not isinstance(index, int):
            print("Converting Index to integer")
            try:
                index = int(index)
            except ValueError:
                return "Index cannot be converted to an integer"

        return lst[index]

    except IndexError:
        return "Index out of range"

    finally:
        print("Operation completed")



if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(safe_list_access(3, 1))
    print(safe_list_access(numbers, 1))
    print(safe_list_access(numbers, '1'))
    print(safe_list_access(numbers, 'abc'))
    print(safe_list_access(numbers, 5))
    print(safe_list_access(numbers, '5'))