from a8_ex2 import Electric_Circuits

class Energy(Electric_Circuits):
    def __init__(self, x: float, y: float, z: int, current: float, resistance: float, time: int):
        super().__init__(x, y, z)
        self.current = current
        self.resistance = resistance
        self.time = time

    def to_string(self) -> str:
        return (f"Energy: x={self.x}, y={self.y}, z={self.z}, "
                f"current={self.current}, resistance={self.resistance}, time={self.time}")

    def measure(self) -> float:
        return (self.current ** 2) * self.resistance * self.time
