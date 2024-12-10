from requests.utils import add_dict_to_cookiejar


class Vector:
    def __init__(self, components: list[float]):
        for component in components:
            if isinstance(component, int) or isinstance(component, float):
                self.components = components
            else:
                raise TypeError("Vector components must be of type int or float")

    def __repr__(self):
        return f"Vector({self.components})"

    def __str__(self):
        ret = "<"
        i = 1
        for component in self.components:
            if i == len(self.components):
                ret += f"{component}>"
            else:
                ret += f"{component}, "
            i += 1
        return ret

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        else:
            return self.components == other.components

    def __add__(self, other):
        if not isinstance(other, Vector) and len(other.components) == len(self.components):
            return NotImplemented
        else:
            return tuple(other.components[i] + self.components[i] for i in range(len(other.components)))

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other

    def __sub__(self, other):
        t1 = self
        t2 = Vector(tuple((other.components[i] * -1) for i in range(len(other.components))))
        return t1 + t2


if __name__ == "__main__":
    v1 = Vector((1, 2, 3))
    v2 = Vector((4, 5, 6))

    print(v1)
    print(repr(v1))
    print(v1 == v2)
    v3 = v1+v2
    print(v3)
    v4 = v1 - v2
    print(v4)
