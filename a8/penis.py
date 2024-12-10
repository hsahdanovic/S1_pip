from a8_ex2 import Electric_Circuits
from a8_ex3 import Energy
from a8_ex4 import Charge_Flow
from a8_ex5 import Power

s = Electric_Circuits(4, 9, 1)
print(s.to_string())
print("Electric Circuits measurement:", s.measure())
e = Energy(1, 2, 3, 0.5, 20, 10)
print(e.to_string())
print("Energy measurement:", e.measure(), "joules")
c = Charge_Flow(5, 2, 2, 0.5, 10)
print(c.to_string())
print("Charge Flow measurement:", c.measure(), "coulombs")
p = Power(5, 2, 2, 0.5, 10)
print(p.to_string())
print("Power measurement:", p.measure(), "watts")
