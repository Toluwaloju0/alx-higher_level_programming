#!/usr/bin/python3
"""A module to create a new class"""


from json import dumps, loads


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

    @classmethod
    def save_to_file(cls, list_objs):
        """A function to save a class to a file"""

        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)

        my_list = []

        for a in list_objs:
            my_list.append(a.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as a:
            a.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """A function to return a list of dictionaries"""

        if json_string is None:
            return []

        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A function to create a new class"""

        if cls.__name__ == "Rectangle":
            a = cls(1, 1)
        elif cls.__name__ == "Square":
            a = cls(1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """To load classes attributes from a string"""

        filename = "{}.json".format(cls.__name__)
        my_list = []
        my_objs = []

        try:
            with open(filename, mode='r', encoding='utf-8') as a:
                my_list = Base.from_json_string(a.read())

            if len(my_list) == 0:
                return []
            for lists in my_list:
                my_objs.append(cls.create(lists))

        except FileNotFoundError:
            my_list = []

        finally:
            return my_objs
