start = int(input("Start:"))
stop = int(input("Stop:"))
step = int(input("Step:"))


even = 0
odd= 0
end = stop - step*5
count = 0
loop = range(start, stop+1, step)

for i in loop:
    if i % 2 == 0:
        even += i
    else:
        odd += i * count
    if count < 5 or i > end:
        print(f"Index: {count}, Value: {i}")
    count += 1

print(f"Sum of all even values: {even}")
print(f"Sum of all odd multiplied values: {odd}")

