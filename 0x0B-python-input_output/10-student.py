#!/usr/bin/python3
"""A module to define a student name"""


class Student:
    """A class of name student"""

    def __init__(self, first_name, last_name, age):
        """To set the name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To retrieve the dict of the class"""

        if attrs is None:
            return self.__dict__

        my_dict = {}
        for key, value in self.__dict__.items():
            for a in attrs:
                if a == key:
                    my_dict[a] = value
        return my_dict
