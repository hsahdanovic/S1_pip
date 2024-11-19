def compose(*functions):
    def composed_function(x):
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed_function if functions else lambda x: x

def add_one(x):
    return x + 1

def square(x):
    return x * x

def half(x):
    return x / 2


composed_f = compose()
result = composed_f(3)
print(result)

composed_f = compose(square)
result = composed_f(3)
print(result)

composed_f = compose(half, square, add_one)
result = composed_f(3)
print(result)
