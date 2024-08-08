#!/usr/bin/python3
"""A module to post using json"""


import requests
import sys


try:
    res = requests.post(sys.argv[1], json=sys.argv[2])
    if res.status_code == 204:
        print("No result")
    else:
        print(res.json)
except requests.exceptions.JSONDecodeError:
    print("Not a valid JSON")
