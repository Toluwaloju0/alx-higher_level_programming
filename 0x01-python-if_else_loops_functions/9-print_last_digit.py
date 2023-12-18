#!/usr/bin/python3
def print_last_digit(number):
    """To print the last digit of a number."""
    if number < 0:
        number = 10 - (number % 10)
    else:
        number = number % 10
    print(number, end="")
    return (number)
