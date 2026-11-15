#!/usr/bin/python3
"""Module that defines a function to get a dictionary for JSON."""

def class_to_json(obj):
    """Return the dictionary description of an object for JSON."""
    return obj.__dict__
