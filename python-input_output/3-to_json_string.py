#!/usr/bin/python3
"""Module that defines a function returning a JSON string of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return json.dumps(my_obj)
