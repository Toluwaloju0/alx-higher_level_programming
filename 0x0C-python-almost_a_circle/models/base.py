#!/usr/bin/python3
"""A module to create a new class"""


class Base:
    """A new class called Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """A unction to initialize the class"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
