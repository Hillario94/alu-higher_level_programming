#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Class that is the base of the geometry classes."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")
