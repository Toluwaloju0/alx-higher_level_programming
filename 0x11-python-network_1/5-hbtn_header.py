#!/usr/bin/python3
"""A module to print a header in a get request"""


import requests
import sys


res = requests.get(sys.argv[1])
print(res.headers['X-Request-Id'])
