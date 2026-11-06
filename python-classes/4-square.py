#!/usr/bin/python3
"""This module defines a Square class with getter and setter for size."""

class Square:
    """This class defines a square with controlled access to size."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional validated size.

        Args:
            size (int): The size of the square, must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size to set, must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square.

        Returns:
            The area of the square computed as size squared.
        """
        return self.__size ** 2
