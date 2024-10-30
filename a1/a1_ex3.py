r = float(input("Radius (in metres): "))
h = float(input("Heigth (in metres): "))
pi = 3.14159

surface = 2 * r * pi * h + r**2 * pi * 2
volume = r**2 * pi * h
water = volume * 0.9
paint = surface * 0.65
plates = int(surface//2 + int(surface)%2)

print(f"Surface area of the tank: {surface: .2f}")
print(f"Volume of the tank: {volume: .2f}")
print(f"Amount of water needed: {water: .2f}")
print(f"Litres of paint needed: {paint: .2f}")
print(f"Number of plates needed: {plates}")