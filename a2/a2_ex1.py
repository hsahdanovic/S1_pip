employment = int(input("Enter employment years (>0):"))
department = int(input("Enter department (10-99):"))
bonus = 0;

if employment > 0 and 10 <= department <= 99:
    if employment < 1:
        print("Invalid Input")
        exit(0)
    elif employment < 2:
        bonus += 200
    elif 2 <= employment <= 3:
        bonus += 300
    elif employment > 3:
        bonus += 400
        if 1 <= department % 10 <= 5:
            bonus *= 1.1
        elif 6 <= department % 10 <= 9:
            bonus *= 1.2
else:
    print("Invalid Input")
    exit(0)

print(f"Bonus for {employment} years of employment in department {department}: {bonus: .2f}")