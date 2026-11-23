#!/usr/bin/python3
"""Module for add_integer.

Provides a function that adds two
integers or floats.
"""


def add_integer(a, b=98):
    """Add two numbers.

    Casts floats to int."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
