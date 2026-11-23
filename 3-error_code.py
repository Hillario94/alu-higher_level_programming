#!/usr/bin/python3
"""Displays body or Error code on HTTPError."""
import sys
import urllib.error
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
