#!/usr/bin/python3
"""Unittests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove files created by the tests."""
        for n in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(n):
                os.remove(n)

    def test_base_auto_id(self):
        """Test Base() assigns an id automatically."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_base_id_plus_one(self):
        """Test Base() assigns the previous id + 1."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_89(self):
        """Test Base(89) saves the id passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_id_12(self):
        """Test Base.to_json_string([{'id': 12}])."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_type(self):
        """Test Base.to_json_string([{'id': 12}]) returns a string."""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        """Test Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_id_89(self):
        """Test Base.from_json_string('[{"id": 89}]')."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_from_json_string_type(self):
        """Test Base.from_json_string('[{"id": 89}]') returns a list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)

    def test_create_rectangle(self):
        """Test Rectangle.create with a dictionary."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")

    def test_load_rectangle_missing(self):
        """Test Rectangle.load_from_file() when the file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_square_exists(self):
        """Test Square.load_from_file() when the file exists."""
        with open("Square.json", "w") as f:
            f.write('[{"id": 5, "size": 5, "x": 0, "y": 0}]')
        self.assertEqual(str(Square.load_from_file()[0]),
                         "[Square] (5) 0/0 - 5")


if __name__ == "__main__":
    unittest.main()
