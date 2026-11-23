#!/usr/bin/python3
"""Module that adds two integers.

This module provides a function that adds two integers or floats
after casting floats to integers, with type validation.
"""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: first integer or float.
        b: second integer or float, defaults to 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
