#!/usr/bin/python3
"""Module that defines the Base class used to manage ids and JSON files."""
import csv
import json


class Base:
    """Base class that manages the id attribute of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance with the given id or an automatic one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        if list_objs is None:
            list_objs = []
        data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(cls.__name__ + ".json", "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with all attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file."""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                data = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of objects to a CSV file named <Class name>.csv."""
        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        else:
            fields = ["id", "width", "height", "x", "y"]
        with open(cls.__name__ + ".csv", "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs or []:
                data = obj.to_dictionary()
                writer.writerow([data[k] for k in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class name>.csv."""
        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        else:
            fields = ["id", "width", "height", "x", "y"]
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as f:
                rows = list(csv.reader(f))
        except FileNotFoundError:
            return []
        return [cls.create(**dict(zip(fields, map(int, row))))
                for row in rows if row]
