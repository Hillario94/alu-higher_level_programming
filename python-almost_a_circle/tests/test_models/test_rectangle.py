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
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_inheritance(self):
        """Test that Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_rectangle_1_2(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 0, 0, 1))

    def test_rectangle_1_2_3(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.x, r.y), (3, 0))

    def test_rectangle_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.x, r.y), (3, 4))

    def test_rectangle_1_2_3_4_5(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_no_arg(self):
        """Test Rectangle()."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_1(self):
        """Test Rectangle(1)."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_six_args(self):
        """Test Rectangle(1, 2, 3, 4, 5, 6)."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rectangle_str_1_2(self):
        """Test Rectangle("1", 2)."""
        with self.assertRaisesRegex(
                TypeError, "^width must be an integer$"):
            Rectangle("1", 2)

    def test_rectangle_1_str_2(self):
        """Test Rectangle(1, "2")."""
        with self.assertRaisesRegex(
                TypeError, "^height must be an integer$"):
            Rectangle(1, "2")

    def test_rectangle_1_2_str_3(self):
        """Test Rectangle(1, 2, "3")."""
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            Rectangle(1, 2, "3")

    def test_rectangle_1_2_3_str_4(self):
        """Test Rectangle(1, 2, 3, "4")."""
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_neg_1_2(self):
        """Test Rectangle(-1, 2)."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Rectangle(-1, 2)

    def test_rectangle_1_neg_2(self):
        """Test Rectangle(1, -2)."""
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            Rectangle(1, -2)

    def test_rectangle_1_2_neg_3(self):
        """Test Rectangle(1, 2, -3)."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Rectangle(1, 2, -3)

    def test_rectangle_1_2_3_neg_4(self):
        """Test Rectangle(1, 2, 3, -4)."""
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_0_2(self):
        """Test Rectangle(0, 2)."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Rectangle(0, 2)

    def test_rectangle_1_0(self):
        """Test Rectangle(1, 0)."""
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            Rectangle(1, 0)

    def test_other_bad_types(self):
        """Test None, float, list and dict values."""
        for bad in (None, 1.5, [1], {}, (1,), True):
            with self.assertRaises(TypeError):
                Rectangle(bad, 1)
            with self.assertRaises(TypeError):
                Rectangle(1, bad)
            with self.assertRaises(TypeError):
                Rectangle(1, 1, bad)
            with self.assertRaises(TypeError):
                Rectangle(1, 1, 0, bad)

    def test_setters(self):
        """Test the getters and setters with valid values."""
        r = Rectangle(1, 1)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_setter_errors(self):
        """Test the setters with invalid values."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """Test area() of Rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test display() of Rectangle."""
        self.assertEqual(capture(Rectangle(4, 2).display), "####\n####\n")
        self.assertEqual(capture(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(capture(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_str_method(self):
        """Test __str__() of Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Test update with positional arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_skip_kwargs(self):
        """Test that kwargs are skipped when args exist."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(5, width=100)
        self.assertEqual(str(r), "[Rectangle] (5) 0/0 - 1/1")

    def test_update_invalid_values(self):
        """Test that update validates values."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(1, 1, -1)

    def test_to_dictionary(self):
        """Test to_dictionary() of Rectangle."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """Test that a dictionary can update another instance."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_create_id(self):
        """Test Rectangle.create(**{'id': 89})."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_id_width(self):
        """Test Rectangle.create with id and width."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_id_width_height(self):
        """Test Rectangle.create with id, width and height."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")

    def test_create_id_width_height_x(self):
        """Test Rectangle.create with id, width, height and x."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")

    def test_create_all(self):
        """Test Rectangle.create with all attributes."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                Base.from_json_string(f.read()),
                [{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        """Test Rectangle.load_from_file() without a file."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test Rectangle.load_from_file() with an existing file."""
        with open("Rectangle.json", "w") as f:
            f.write('[{"id": 5, "width": 1, "height": 2, '
                    '"x": 3, "y": 4}]')
        out = Rectangle.load_from_file()
        self.assertIsInstance(out[0], Rectangle)
        self.assertEqual(str(out[0]), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
