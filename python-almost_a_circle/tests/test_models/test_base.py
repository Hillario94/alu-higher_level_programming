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
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_base_no_arg(self):
        """Test Base() three times."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual((b1.id, b2.id, b3.id), (1, 2, 3))

    def test_base_none(self):
        """Test Base(None)."""
        self.assertEqual(Base(None).id, 1)

    def test_base_12(self):
        """Test Base(12)."""
        self.assertEqual(Base(12).id, 12)

    def test_base_given_id_keeps_counter(self):
        """Test that a given id does not change the counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_base_other_ids(self):
        """Test Base with 0, a negative number, a string and a list."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("1").id, "1")
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_base_two_args(self):
        """Test Base(1, 2)."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_one(self):
        """Test Base.to_json_string([{'id': 12}])."""
        s = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(s, str)
        self.assertEqual(s, '[{"id": 12}]')

    def test_to_json_string_two(self):
        """Test Base.to_json_string with two dictionaries."""
        self.assertEqual(Base.to_json_string([{'id': 1}, {'id': 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_no_arg(self):
        """Test Base.to_json_string()."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("")."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_empty_list(self):
        """Test Base.from_json_string("[]")."""
        out = Base.from_json_string("[]")
        self.assertIsInstance(out, list)
        self.assertEqual(out, [])

    def test_from_json_string_one(self):
        """Test Base.from_json_string with one dictionary."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_from_json_string_two(self):
        """Test Base.from_json_string with two dictionaries."""
        self.assertEqual(
            Base.from_json_string('[{"id": 1}, {"id": 2}]'),
            [{"id": 1}, {"id": 2}])

    def test_from_json_string_no_arg(self):
        """Test Base.from_json_string()."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_json_round_trip(self):
        """Test that to_json_string and from_json_string are inverse."""
        data = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(
            Base.from_json_string(Base.to_json_string(data)), data)

    def test_create_rectangle(self):
        """Test create with a Rectangle dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_create_square(self):
        """Test create with a Square dictionary."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_load_from_file_missing(self):
        """Test load_from_file() without any file."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangles(self):
        """Test load_from_file() with rectangles."""
        with open("Rectangle.json", "w") as f:
            f.write('[{"id": 1, "width": 10, "height": 7, "x": 2, '
                    '"y": 8}, {"id": 2, "width": 2, "height": 4, '
                    '"x": 0, "y": 0}]')
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertEqual(str(out[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(out[1]), "[Rectangle] (2) 0/0 - 2/4")

    def test_load_from_file_squares(self):
        """Test load_from_file() with squares."""
        with open("Square.json", "w") as f:
            f.write('[{"id": 5, "size": 5, "x": 0, "y": 0}, '
                    '{"id": 6, "size": 7, "x": 9, "y": 1}]')
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertEqual(str(out[0]), "[Square] (5) 0/0 - 5")
        self.assertEqual(str(out[1]), "[Square] (6) 9/1 - 7")


    def test_save_squares_base(self):
        """Test Square.save_to_file with one square."""
        s1 = Square(5)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_empty_list_base(self):
        """Test Square.save_to_file with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_none_base(self):
        """Test Square.save_to_file with None."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
