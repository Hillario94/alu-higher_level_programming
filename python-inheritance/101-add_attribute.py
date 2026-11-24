#!/usr/bin/python3
"""Module that defines a function adding an attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj, or raise TypeError if not possible."""
    if not hasattr(obj, "__dict__") and not hasattr(type(obj), name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
