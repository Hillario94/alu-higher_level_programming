#!/bin/bash
# Displays the body of the response only if status is 200, following redirections
curl -s -L -f "$1"
