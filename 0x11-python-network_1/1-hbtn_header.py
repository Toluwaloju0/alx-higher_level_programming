#!/usr/bin/python3
"""A module to request a url and print the header"""

import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as response:
    page_header = response.info()
    print(page_header['X-Request-Id'])
