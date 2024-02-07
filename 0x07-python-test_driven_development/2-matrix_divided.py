#!/usr/bin/python3

"""A module that divides a matrix"""


def matrix_divided(matrix, div):
    new_matrix = []

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        if a > 0:
            if len(matrix[a]) != len(matrix[a - 1]):
                raise TypeError("Each row of the matrix must have \
the same size")
        new_matrix.append([])
        for b in matrix[a]:
            if not isinstance(b, (int, float)):
                raise TypeError("matrix must be a matrix (list\
 of lists) of integers/floats")
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            new_matrix[a].append(round((b / div), 2))
    return new_matrix
