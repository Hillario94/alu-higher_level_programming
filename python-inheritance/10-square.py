#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
