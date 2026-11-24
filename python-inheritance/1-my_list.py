#!/usr/bin/python3
"""Module that defines MyList, a list class able to print itself sorted."""


class MyList(list):
    """Class that extends the built-in list with a sorted printing."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
