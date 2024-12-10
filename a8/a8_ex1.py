class Voltage:
    def __init__(self, current: float, resistance: float):
        self._current = current
        self._resistance = resistance

    @property
    def current(self) -> float:
        return self._current

    @property
    def resistance(self) -> float:
        return self._resistance

    def print(self):
        sign = "+" if self._current > 0 else "-"
        print(f"{sign}{abs(self._current)} amps + {self._resistance} ohms")

    def volt(self) -> float:
        return self._current * self._resistance

    def increase_resistance(self, delta: float):
        if not isinstance(delta, (float, int)):
            raise TypeError(f"Please provide float value instead of {type(delta).__name__}")
        self._resistance += delta

    @staticmethod
    def add_all(volt_obj: "Voltage", *volt_objs: "Voltage") -> "Voltage":
        if not isinstance(volt_obj, Voltage):
            raise TypeError("Can only add objects of type 'Voltage'")

        total_resistance = volt_obj.resistance
        current = volt_obj.current

        for obj in volt_objs:
            if not isinstance(obj, Voltage):
                raise TypeError("Can only add objects of type 'Voltage'")
            if obj.current != current:
                raise ValueError("The current must be equal")
            total_resistance += obj.resistance

        return Voltage(current, total_resistance)


if __name__ == "__main__":
    c1 = Voltage(-5.0, 20)
    c1.print()
    c2 = Voltage(3.0, 4.0)
    c2.print()
    print(c2.volt())

    c1 = Voltage(10.0, 2.0)
    c1.print()
    c2 = Voltage(10.0, 5.0)
    c1.increase_resistance(5)
    c1.print()
    c_sum = Voltage.add_all(c1, c1, c2, Voltage(10.0, 5.0))
    c_sum.print()
    c1.print()
