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
        """Remove the files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        """Test that ids are incremented automatically."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        """Test that a given id is kept."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        """Test that a given id does not change the counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_other_id_values(self):
        """Test ids that are zero, negative or not integers."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("abc").id, "abc")
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_too_many_args(self):
        """Test that too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        s = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertIsInstance(s, str)
        self.assertEqual(s, '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_no_arg(self):
        """Test to_json_string without argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """Test from_json_string with a valid string."""
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])

    def test_from_json_string_no_arg(self):
        """Test from_json_string without argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_json_round_trip(self):
        """Test that to_json_string and from_json_string are inverse."""
        data = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(
            Base.from_json_string(Base.to_json_string(data)), data)

    def test_save_rectangles(self):
        """Test save_to_file with rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """Test save_to_file with squares."""
        s1 = Square(5)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        """Test save_to_file with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        """Test that save_to_file overwrites an existing file."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        Rectangle.save_to_file([Rectangle(3, 3)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 1)

    def test_save_no_arg(self):
        """Test save_to_file without argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_create_rectangle(self):
        """Test create with a Rectangle dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertEqual(str(r1), str(r2))
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_create_square(self):
        """Test create with a Square dictionary."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_load_missing_file(self):
        """Test load_from_file when the file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Test load_from_file with rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertIsInstance(out[0], Rectangle)
        self.assertIsNot(out[0], r1)
        self.assertEqual(str(out[0]), str(r1))
        self.assertEqual(str(out[1]), str(r2))

    def test_load_squares(self):
        """Test load_from_file with squares."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertIsInstance(out[0], Square)
        self.assertEqual(str(out[0]), str(s1))
        self.assertEqual(str(out[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
