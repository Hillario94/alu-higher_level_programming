#!/usr/bin/python3
"""Module that defines a Square class with a size and a position."""


class Square:
    """Class that defines a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square using the validated setters."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating the value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after checking it is a tuple of 2 integers."""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # using the position as an offset."""
        if self.__size == 0:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
