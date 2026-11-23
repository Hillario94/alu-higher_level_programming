#!/usr/bin/python3
"""Displays the value of X-Request-Id header."""
import sys

import requests

r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
