#!/usr/bin/python3
"""Module that defines a function giving the dictionary of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON use."""
    return obj.__dict__
