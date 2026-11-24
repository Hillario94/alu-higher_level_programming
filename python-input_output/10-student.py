#!/usr/bin/python3
"""Module that defines a Student class.

The Student class stores a first name, a last name and an age, and can
return a dictionary description of itself for JSON serialization.
"""


class Student:
    """Class that defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary of the student, filtered by attrs."""
        if isinstance(attrs, list):
            if all(isinstance(a, str) for a in attrs):
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
