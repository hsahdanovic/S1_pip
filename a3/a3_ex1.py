rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


print("   ", end="")
for i in range(0, 2):
    for c in range(0, cols):
        if i == 0:
            print(f" {c}", end="")
        else:
            print(f"--", end="")
    if i == 0:
        print("\n   ", end="")
    else:
        print("-")

for c in range(0, cols):
    print(f"{c} |", end="")
    for r in range(0, rows):
        print(f" {'X' if (c + r) % 2 == 0 else 'O'}", end="")
        if r+1 == rows:
            print(f" |")

print("   ", end="")
for c in range(0, cols):
    print(f"--", end="")
print("-")
