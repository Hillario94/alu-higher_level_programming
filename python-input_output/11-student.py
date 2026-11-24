#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded.

The Student class stores a first name, a last name and an age, can return
a dictionary description of itself, and can rebuild itself from one.
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

    def reload_from_json(self, json):
        """Replace the attributes of the student using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
