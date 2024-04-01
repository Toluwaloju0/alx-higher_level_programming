#!/usr/bin/python3
class Node:
    """A class of node
    """
    def __init__(self, data, next_node=None):
        """to set the initial values of the class
        Args:
            data (int): the integer to be added
            next_node (Node): pointer to the next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
    @property
    def data(self):
        """to get the data of the class
        """
        return node.__data

    @data.setter
    def data(self, value):
        """To set the data to a different value
        Args:
            value (int): the number to change the datat into
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """to get the next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """to set the next_node to a different value
        Args:
            value (Node): the next_node
        """
        if type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """To define a singly linked list in python
    """
    def __init__(self):
        """To set the initial values of the list
        """
        self.__head = 

    def sorted_insert(self, value):
        """to add a node into the linked list
        """
        print(value)
