#!/usr/bin/python3
"""A module to print a text"""


def text_indentation(text=""):
    """A function to seperare a string based on characters
    Args:
        text(str): the text to be seperated
    """

    a = 0
    if text is None:
        return None
    if type(text) is not str:
        raise TypeError("text must be a string")

    if len(text) == 0:
        return None
    if text[0] == ' ':
        a = a + 1
        while text[a]:
            if text[a] == ' ':
                a = a + 1
                continue
            break
    b = len(text) - 1
    while b > 0:
        if text[b] == ' ':
            b = b - 1
            continue
        break
    while a <= b:
        if text[a] == '.' or text[a] == '?' or text[a] == ':':
            print(text[a] + '\n')
            a = a + 1
            while text[a] and a <= b:
                if text[a] == ' ':
                    a = a + 1
                    continue
                break
            continue
        if a == b:
            print(text[a] + '\n')
            break
        print(text[a], end='')
        a = a + 1
