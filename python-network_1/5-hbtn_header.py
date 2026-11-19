#!/usr/bin/python3
"""Displays the value of X-Request-Id from the response header of a URL"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
