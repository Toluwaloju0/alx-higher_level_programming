#!/usr/bin/python3
"""A module to make a post request"""


import urllib.request, urllib.parse
import sys


url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.encode(values)
data = data.encode('utf-8')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    page = response.read()
    print(page.decode('utf-8'))
