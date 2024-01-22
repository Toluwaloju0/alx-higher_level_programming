#!/usr/bin/python3
"""A module that loads to a json file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
a = 1

try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    pass
finally:
    for a in range(1, len(sys.argv)):
        my_list.append(sys.argv[a])

    save_to_json_file(my_list, "add_item.json")
