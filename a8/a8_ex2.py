class Electric_Circuits:
    def __init__(self, x: float, y: float, z: int):
        self.x = x
        self.y = y
        self.z = z

    def to_string(self) -> str:
        return f"{self.__class__.__name__}: x={self.x}, y={self.y}, z={self.z}"

    def measure(self) -> float:
        raise NotImplementedError("The 'measure' method must be implemented in a subclass.")
