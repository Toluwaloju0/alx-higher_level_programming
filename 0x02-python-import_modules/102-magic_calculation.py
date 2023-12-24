def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(1, 6):
            c += i
        return c
    else:
        return a - b
