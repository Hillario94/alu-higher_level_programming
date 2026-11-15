#!/usr/bin/python3
"""Module that defines a class Student that can reload from JSON."""

class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            if all(isinstance(a, str) for a in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of a Student instance from JSON."""
        for key, value in json.items():
            setattr(self, key, value)
