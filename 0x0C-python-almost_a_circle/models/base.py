#!/usr/bin/python3
"""A module to create a new class"""


from json import dumps


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """To convert a dictionary list to a json strong"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return dumps(list_dictionaries)
