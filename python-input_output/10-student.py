#!/usr/bin/python3
"""Module that defines a class Student with filtered JSON."""

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
                new_dict = {}
                for k in attrs:
                    if hasattr(self, k):
                        new_dict[k] = getattr(self, k)
                return new_dict
        return self.__dict__
