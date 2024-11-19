def numerical_sequence():
        n = 0
        i = 1

        while True:
            n += i
            i += 1
            yield n


sequence = numerical_sequence()
for i in range(1, 11):
        print(f'number at {i}: {next(sequence)}')