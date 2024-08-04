#!/usr/bin/python3
"""A module to get a url response using request"""


import requests


res = requests.get("https://alx-intranet.hbtn.io/status")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))
