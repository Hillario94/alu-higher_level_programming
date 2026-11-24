#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """Class that is the base of the geometry classes."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
