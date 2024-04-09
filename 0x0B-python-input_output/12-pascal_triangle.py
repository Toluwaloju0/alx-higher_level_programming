#!/usr/bin/python3
"""A  module to get the pascal triangle"""


def pascal_triangle(n):
    my_list = []
    a = 0

    if n == 0:
        return my_list

    while a < n:
        my_list.append([])
        b = 0
        while b <= a:
            if b == 0 or b == a:
                my_list[a].append(1)
                b += 1
                continue
            my_list[a].append(my_list[a - 1][b] + my_list[a - 1][b - 1])
            b += 1
        a += 1

    return my_list
