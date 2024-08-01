#!/usr/bin/python3
"""A module to descrpbe a function"""


def find_peak(list_of_integers):
    """A functiojn to find the peak in a list of integers
    Args:
        list_of_integers: A list containing only integers
    """

    a = 1
    peak = 0

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]

    for a in range(len(list_of_integers)):
            if list_of_integers[a] > peak:
                peak = list_of_integers[a]
    return peak
