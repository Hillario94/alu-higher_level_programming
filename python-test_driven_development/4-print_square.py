#!/usr/bin/python3
"""Module that prints a square.

This module provides a function that prints a square
made of the character # with a given size.
"""

def print_square(size):
    """Print a square with the character #.

    Args:
        size: size length of the square as an integer.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
