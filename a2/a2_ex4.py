size= int(input())
if size%2==0:
    size += 1

start = int(size/2)
end = size/2
step = -1
space = 0
while start <= end:
    if space>0:
        print(" " * start + "*" + " " * (space-1) + "*")
    else:
        print(" "*start+"*")
    if start == 0:
        step *= -1
    space += (-1*step * 2)
    start += step
