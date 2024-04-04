#!/usr/bin/python3
"""A module to multiply two matrices toghether"""


def matrix_mul(m_a, m_b):
    """A function to multiply two matrices toghether
    Args:
        m_a(list of list): the first matrix
        m_b(list of list): the second matrix
    Return: A nuw matrix containing the multiplication of a and b
    """

    # To check the type of m_a and m_b
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # to check if m_a or m_b is empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # To check if each elements in m_a is a list, the value type and length
    for a in range(len(m_a)):
        if type(m_a[a]) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a[a]) == 0:
            raise ValueError("m_a can't be empty")
        for b in m_a[a]:
            if not isinstance(b, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if a > 1:
            if len(m_a[a]) != len(m_a[a - 1]):
                raise TypeError("each row of m_a must be of the same")

    # To check if each elements in m_b is a list, the value type and length
    for a in range(len(m_b)):
        if type(m_b[a]) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b[a]) == 0:
            raise ValueError("m_b can't be empty")
        for b in m_b[a]:
            if not isinstance(b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if a > 1:
            if len(m_b[a]) != len(m_b[a - 1]):
                raise TypeError("each row of m_b must be of the same")

    # To check if the rowa and columns are of the same size
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # The multiplication method
    my_matrix = [[0 for _ in range(len(m_a))] for _ in range(len(m_b[0]))]

