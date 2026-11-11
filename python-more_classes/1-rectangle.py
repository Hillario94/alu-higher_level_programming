#!/usr/bin/python3
"""This module defines a Rectangle class for a rectangle."""


class Rectangle:
    """This class defines a rectangle with validated dimensions."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle, must be >= 0.
            height (int): The height of the rectangle, must be >= 0.
        """
        self.width = width
        self.height = height

    @property

    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            The current width of the rectangle.
        """
        return self.__width

    @width.setter

    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The new width to set, must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property

    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            The current height of the rectangle.
        """
        return self.__height

    @height.setter

    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The new height to set, must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
