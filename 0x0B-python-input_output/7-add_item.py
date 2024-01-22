#!/usr/bin/python3
"""A module that loads to a json file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


for a in sys.argv:
    save_to_json_file(a, "add_item.json")
