#!/usr/bin/python3
"""Sends POST to search_user with q and displays result."""
import sys

import requests

q = sys.argv[1] if len(sys.argv) > 1 else ""
r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    data = r.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
