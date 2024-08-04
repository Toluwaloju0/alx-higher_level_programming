#!/usr/bin/python3
"""A module to fetch a url"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    alx_intranet = response.read()
    print("\t- type: {}".format(type(alx_intranet)))
    print("\t- content: {}".format(alx_intranet))
    print("\t- utf8 content: {}".format(alx_intranet.decode('utf-8')))
