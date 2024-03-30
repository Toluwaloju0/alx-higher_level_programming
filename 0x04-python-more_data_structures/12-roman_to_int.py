#!/usr/bin/python3
def roman_to_int(roman_string):
    A = 0
    a = 0
    b = 6
    c = 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    if not isinstance(roman_string, (str)) or roman_string is None:
        return A
    while a < len(roman_string):
        c = 0
        for key, value in num.items():
            c = c + 1
            if roman_string[a] == key:
                A = A + value
                break
        if b < c:
            key = num_list[b - 1]
            A = A - (num[key] * 2)
        b = c
        a = a + 1
    return A
