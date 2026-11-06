#!/usr/bin/python3
"""This module defines a Square class that represents a square by size."""

class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a Square instance with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size
