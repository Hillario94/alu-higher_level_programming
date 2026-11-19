#!/bin/bash
# Displays all HTTP methods the server at the given URL will accept
curl -sI -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2- | tr -d '\r'
