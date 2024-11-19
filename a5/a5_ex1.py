def analyze_and_update_collection(my_list, my_set=set()):

    assert my_list, "Aborted as my_list must not be empty"
    assert [isinstance(i, int) for i in my_list], "Aborted as my_list contains non integer values"


    n = len(my_list)
    print(f"Thle last element of my_list is {my_list[n]}")

    if my_set is set(my_list):
        print("my_set and my_list contain the same elements")


items1 = [1,2,3,4,5]
items2 = [2,4,6]

s = analyze_and_update_collection(items1)
print('Current set:', s)
s = analyze_and_update_collection(items2)
print('Current set:', s)
s = analyze_and_update_collection(items1, my_set=set(items1))
print('Current set:', s)
s = analyze_and_update_collection(items1, my_set=set(items2))
print('Current set:', s)

try:
    s = analyze_and_update_collection([])
except AssertionError as e:
    print(e)
try:
    s = analyze_and_update_collection([str(i) for i in items1])
except AssertionError as e:
    print(e)