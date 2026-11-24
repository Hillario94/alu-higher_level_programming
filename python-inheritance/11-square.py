#!/usr/bin/python3
"""Module that defines a Square class with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square with a private size."""

    def __init__(self, size):
        """Initialize a square after validating its size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
