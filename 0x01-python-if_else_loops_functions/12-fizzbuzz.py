#!/usr/bin/python3
def fizzbuzz():
    """To print Fizz Buzz up to 100."""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ", end="")
            continue
        elif i % 5 == 0:
            print("Buzz ", end="")
            continue
        elif i % 3 == 0:
            print("Fizz ", end="")
            continue
        print(i, " ", end="")
