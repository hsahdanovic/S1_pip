from a8_ex2 import Electric_Circuits

class Charge_Flow(Electric_Circuits):
    def __init__(self, x: float, y: float, z: int, current: float, time: int):
        super().__init__(x, y, z)
        self.current = current
        self.time = time

    def to_string(self) -> str:
        return f"Charge_Flow: x={self.x}, y={self.y}, z={self.z}, current={self.current}, time={self.time}"

    def measure(self) -> float:
        return self.current * self.time