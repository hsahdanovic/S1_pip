_all = []
_first = []
_second = []
_sorted = []

while True:
    inp = input("Enter element or 'x' when done: ")
    if inp == 'x':
        break
    _all.append(inp)

print(f"All: {_all}")
print(f"First half: {_first}")
print(f"Second half: {_second}")
print(f"Sorted common words: {_sorted}")
