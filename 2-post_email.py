#!/usr/bin/python3
"""Sends POST request with email and displays body."""
import sys
import urllib.parse
import urllib.request

data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
req = urllib.request.Request(sys.argv[1], data=data, method='POST')
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
