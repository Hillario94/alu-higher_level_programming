#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """Class that defines a square by its private size."""

    def __init__(self, size):
        """Initialize a new square with the given size, without checks."""
        self.__size = size
