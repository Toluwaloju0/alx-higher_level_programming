#!/usr/bin/python3
"""A module to insert text after a word"""


def append_after(filename="", search_string="", new_string=""):
    """A function to add text after a search_string
    Args:
        filename (str): The name of thye file
        search_string (str): The string to be searche for
        new_string (str): the string to be appended
    """

    with open(filename, mode='r', encoding="utf-8") as a:
        content = a.readlines()

    text_list = []
    for old_text in content:
        text_list.append(old_text)
        if search_string in old_text:
            text_list.append(new_string)

    with open(filename, mode='w', encoding="utf-8") as a:
        a.writelines(text_list)
