#!/usr/bin/python3
"""Module that defines MyInt, an int class with inverted comparisons."""


class MyInt(int):
    """Class that inherits from int and inverts == and !=."""

    def __eq__(self, other):
        """Return True when the values differ, as an inverted equality."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal, as an inverted inequality."""
        return int.__eq__(self, other)
