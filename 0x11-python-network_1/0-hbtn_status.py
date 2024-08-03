#!/usr/bin/python3
"""A module to fetch a url"""


import urllib


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    alx-intranet = response.read()
for each in alx-intranet:
    print("\t-{}".format(each))
