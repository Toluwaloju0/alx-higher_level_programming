#!/usr/bin/python3
"""A module to get id from github"""


import requests
import sys
import json


url = "https://api.github.com/User/{}".format(sys.argv[1])
header = {
        'accept': "application/vnd.github+json",
        'Authorization': "Bearer {}".format(sys.argv[2])
        }
res = requests.get(url, headers=header)
if res.status_code != 200:
    print("None")
    exit()
res_dict = json.loads(res.text)
print(res_dict['id'])
