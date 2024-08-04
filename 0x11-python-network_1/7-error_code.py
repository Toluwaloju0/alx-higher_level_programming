#!/usr/bin/python3
"""A module to print errors if any"""


import requests
import sys


try:
    res = requests.get(sys.argv[1])
    print(res.text)
except requests.HTTPError as e:
    print(f"Error code: {e.code}")
