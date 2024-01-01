#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - To square a matrix
    matrix - a list of lists
    """
    a = 0

    if matrix is None:
        return None
    new_matrix = []
    for p in matrix:
        new_matrix.append([])
        for j in p:
            new_matrix[a].append(j ** 2)
        a += 1
    return new_matrix
