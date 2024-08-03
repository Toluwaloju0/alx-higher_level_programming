#!/usr/bin/python3
"""A module to fetch a url"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    alx_intranet = response.read()
for each in alx-intranet:
    print("\t-{}".format(each))
