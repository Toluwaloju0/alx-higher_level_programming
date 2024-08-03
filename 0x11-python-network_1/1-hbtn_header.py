#!/usr/bin/python3
"""A module to request a url and print the header"""

import sys
import urllib


with urllib.request.urlopen(sys.argv[1]) as response:
    opened_url = response.read()
for 
