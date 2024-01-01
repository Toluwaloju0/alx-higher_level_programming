#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - To search and replace an element in a list
    my_list: the list to be searched
    search: the element to search for
    replace: the element to replace
    """

    if my_list is None:
        return None
    new_list = []
    for a in my_list:
        if a == search:
            new_list.append(replace)
            continue
        new_list.append(a)
    return new_list
