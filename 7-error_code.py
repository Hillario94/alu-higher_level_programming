#!/usr/bin/python3
"""Displays body or Error code if status >= 400."""
import sys

import requests

r = requests.get(sys.argv[1])
if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)
