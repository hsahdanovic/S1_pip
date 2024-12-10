from a8_ex3 import Energy

class Power(Energy):
    def __init__(self, x: float, y: float, z: int, current: float, resistance: float):
        super().__init__(x, y, z, current, resistance, 1) 

    def to_string(self) -> str:
        return f"Power: x={self.x}, y={self.y}, z={self.z}, current={self.current}, resistance={self.resistance}, time={self.time}"

    def measure(self) -> float:
        return self.current**2 * self.resistance