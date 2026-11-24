#!/usr/bin/python3
"""Module that defines a Square class with a validated size."""


class Square:
    """Class that defines a square by its private and validated size."""

    def __init__(self, size=0):
        """Initialize a new square after validating the given size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
