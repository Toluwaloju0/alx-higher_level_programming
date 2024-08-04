#!/usr/bin/python3
"""A module to make a post request and print the response"""


import requests
import sys


header = {'email': sys.argv[2]}

res = requests.post(sys.argv[1], data=header)

print(res.text)
