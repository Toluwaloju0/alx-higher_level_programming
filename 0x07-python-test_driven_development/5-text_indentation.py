#!/usr/bin/python3
"""A module to print a text"""


def text_indentation(text):
    """A function to seperare a string based on characters
    Args:
        text(str): the text to be seperated
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for a in range(len(text)):
        if text[a] == '.' or text[a] == '?' or text[a] == ':':
            print(text[a] + '\n')
            a = a + 1
            while text[a]:
                if text[a] == ' ':
                    a = a + 1
                    continue
                break
            continue
        print(text[a], end='')
