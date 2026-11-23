#!/usr/bin/python3
"""Module for add_integer.

Provides a function that adds two
integers or floats.
"""


def add_integer(a, b=98):
    """Add two numbers.

    Casts floats to int."""
    if not isinstance(a, (int, float)) or a != a or abs(a) == float("inf"):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or abs(b) == float("inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
