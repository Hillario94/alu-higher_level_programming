#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -s "$1"
