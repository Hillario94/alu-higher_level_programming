#!/usr/bin/python3
"""This module defines a Square class with size and area method."""

class Square:
    """This class defines a square with size and area computation."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional validated size.

        Args:
            size (int): The size of the square, must be >= 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square.

        Returns:
            The area of the square computed as size squared.
        """
        return self.__size ** 2
