#!/usr/bin/python3
"""Module that prints a name.

This module provides a function that prints a full name
in the format My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Args:
        first_name: first name as a string.
        last_name: last name as a string, defaults to "".

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
