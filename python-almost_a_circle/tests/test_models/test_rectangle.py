#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


def capture(func):
    """Return everything printed to stdout while func runs."""
    with patch("sys.stdout", new=io.StringIO()) as out:
        func()
    return out.getvalue()


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove files created by the tests."""
        for n in ("Rectangle.json", "Square.json"):
            if os.path.exists(n):
                os.remove(n)

    def test_1_2(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_1_2_3(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.x, r.y), (3, 0))

    def test_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.x, r.y), (3, 4))

    def test_1_2_3_4_5(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_str_width(self):
        """Test Rectangle("1", 2)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_str_height(self):
        """Test Rectangle(1, "2")."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_str_x(self):
        """Test Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_str_y(self):
        """Test Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_neg_width(self):
        """Test Rectangle(-1, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_neg_height(self):
        """Test Rectangle(1, -2)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Test Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Test Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_neg_x(self):
        """Test Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_neg_y(self):
        """Test Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area()."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str_method(self):
        """Test __str__() for Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        """Test display() without x and y."""
        self.assertEqual(capture(Rectangle(2, 2).display), "##\n##\n")

    def test_display_without_y(self):
        """Test display() without y."""
        self.assertEqual(capture(Rectangle(2, 2, 1).display), " ##\n ##\n")

    def test_display(self):
        """Test display()."""
        self.assertEqual(capture(Rectangle(1, 1, 1, 1).display), "\n #\n")

    def test_to_dictionary(self):
        """Test to_dictionary() in Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4})

    def test_update_none(self):
        """Test update()."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_89(self):
        """Test update(89)."""
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1)."""
        r = Rectangle(5, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2)."""
        r = Rectangle(5, 5)
        r.update(89, 1, 2)
        self.assertEqual((r.width, r.height), (1, 2))

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3)."""
        r = Rectangle(5, 5)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        """Test update(89, 1, 2, 3, 4)."""
        r = Rectangle(5, 5)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.to_dictionary(),
                         {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89})."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test update(**{'id': 89, 'width': 1})."""
        r = Rectangle(5, 5)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        """Test update(**{'id': 89, 'width': 1, 'height': 2})."""
        r = Rectangle(5, 5)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_x(self):
        """Test update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})."""
        r = Rectangle(5, 5)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_y(self):
        """Test update with id, width, height, x and y."""
        r = Rectangle(5, 5)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_update_args_skip_kwargs(self):
        """Test that kwargs are skipped when args exist."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(5, width=100)
        self.assertEqual(r.width, 1)

    def test_create(self):
        """Test Rectangle.create(**{'id': 89})."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as f:
            self.assertEqual(
                Base.from_json_string(f.read()),
                [{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        """Test Rectangle.load_from_file() when the file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test Rectangle.load_from_file() when the file exists."""
        with open("Rectangle.json", "w") as f:
            f.write('[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')
        self.assertEqual(str(Rectangle.load_from_file()[0]),
                         "[Rectangle] (5) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
