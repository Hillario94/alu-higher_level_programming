#!/usr/bin/python3
"""Module that defines a function to convert an object to JSON."""
import json

def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
