class Voltage:
    def __init__(self, current: float, resistance: float):
        super().__init__()
        self._current = current
        self._resistance = resistance

    def current(self) -> float:
        return self._current

    def resistance(self) -> float:
        return self._resistance

    def print(self):
        sign = "+"
        if self._current < 0:
            sign = ""
        print(f"{sign}{self._current} amps + {self._resistance} ohms")

    def volt(self):
        return self._current * self._resistance

    def increase_resistance(self, data: float):
        if type(data-self._resistance).__name__ is not float:
            raise TypeError(f"Please provide float value instead of {type(data).__name__}")
        else:
            self._resistance += data

    @staticmethod
    def add_all(volt_obj: "Voltage", *volt_objs: "Voltage") -> "Voltage":
        val = 0
        for obj in volt_objs:
            if obj._current == volt_obj._current:
                if type(obj).__name__ != "Voltage":
                    raise TypeError(f"Can only add objects of type 'Voltage'")
                else:
                    val += obj._resistance
            else:
                raise ValueError(f"The current must be equal")

        return Voltage(val, volt_obj._resistance)

if __name__ == "__main__":
    # c1 = Voltage(-5.0, 20)
    # c1.print()
    # c2 = Voltage(3.0, 4.0)
    # c2.print()
    # print(c2.volt())

    c1 = Voltage(10.0, 2.0)
    c1.print()
    c2 = Voltage(10.0, 5.0)
    c1.increase_resistance(5)
    c1.print()
    c_sum = Voltage.add_all(c1, c1, c2, Voltage(10.0, 5.0))
    c_sum.print()
    c1.print()