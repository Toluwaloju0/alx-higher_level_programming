#!/usr/bin/python3
"""To show inheritance in a class"""


class MyList(list):
    """A class that inherits the attributes in List"""

    def print_sorted(self):
        """A function that prints the listin sorted form"""

        a = sorted(self)
        print(a)
