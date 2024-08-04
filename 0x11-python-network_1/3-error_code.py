#!/usr/bin/python3
"""A module to take a url and get a response"""


import urllib.request
import urllib.error
import sys


try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read())
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
