def magic_calculation(a, b):
    if a > b:
        return (a + b)
    else:
        c = b - a
        for i in range(4, 6):
            c = magic_calculation(c, i)
        return c * -1
