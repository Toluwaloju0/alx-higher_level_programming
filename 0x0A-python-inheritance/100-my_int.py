#!/usr/bin/python3
"""A module to create a new class"""


class MyInt(int):
    """The class which inherits from int"""

    def __eq__(self, other):

        return not super().__eq__(other)

    def __ne__(self, other):

        return not super().__ne__(other)
