tmp = 0
number = 1
empty = True

while number < 1000:
    tmp = input("Enter a value (or 'x' to stop): ")
    if tmp.isdigit() and int(tmp) > 0:
        number *= int(tmp)
    elif tmp == "x":
        if empty:
            print(f"Empty sequence")
            exit(0)
        else:
            print(f"Result: {number}")
            exit(0)
    empty = False

print(f"Result has exceeded the value 1000: {number}")
