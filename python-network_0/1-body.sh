#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status code is 200
curl -sf "$1"
