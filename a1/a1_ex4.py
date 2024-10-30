chairs = int(input("Input the number of ordered chairs: "))
tables = int(input("Input the number of ordered tables: "))
lamps = int(input("Input the number of ordered lamps: "))

chairPrice = 49.99
tablePrice = 199.99
lampPrice = 29.99

total = chairs * chairPrice + tables * tablePrice + lamps * lampPrice
print("\n" + "-"*33)   asd
print(f"Chairs:{chairs: 4} x{chairPrice: 7.2f} = {chairs * chairPrice: 10.2f}")
print(f"Tables:{tables: 4} x{tablePrice: 7.2f} = {tables * tablePrice: 10.2f}")
print(f"Lamps: {lamps: 4} x{lampPrice: 7.2f} = {lamps * lampPrice: 10.2f}")
print("-"*33)
print(f"Total:{" ":17}{total: 10.2f}")
print("="*33)
