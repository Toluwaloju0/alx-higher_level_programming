#!/usr/bin/python3
"""A module to define a student name"""


class Student:
    """A class of name student"""

    def __init__(self, first_name, last_name, age):
        """To set the name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To retrieve the dict of the class"""

        return self.__dict__
