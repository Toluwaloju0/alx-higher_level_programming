#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    if tuple_a is None or len(tuple_a) == 0:
        tuple_a = 0, 0
    if tuple_b is None or len(tuple_b) == 0:
        tuple_b = 0, 0
    if len(tuple_a) < 2:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        tuple_b = tuple_b[0], 0
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = a, b
    return new_tuple
