#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def capture(func):
    """Return everything printed to stdout while func runs."""
    with patch("sys.stdout", new=io.StringIO()) as out:
        func()
    return out.getvalue()


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Test that Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_square_1(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 0, 0, 1))

    def test_square_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_square_1_2_3_4(self):
        """Test Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_str_1(self):
        """Test Square("1")."""
        with self.assertRaisesRegex(
                TypeError, "^width must be an integer$"):
            Square("1")

    def test_square_1_str_2(self):
        """Test Square(1, "2")."""
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            Square(1, "2")

    def test_square_1_2_str_3(self):
        """Test Square(1, 2, "3")."""
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            Square(1, 2, "3")

    def test_square_neg_1(self):
        """Test Square(-1)."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Square(-1)

    def test_square_1_neg_2(self):
        """Test Square(1, -2)."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Square(1, -2)

    def test_square_1_2_neg_3(self):
        """Test Square(1, 2, -3)."""
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Square(1, 2, -3)

    def test_square_0(self):
        """Test Square(0)."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Square(0)

    def test_square_no_arg(self):
        """Test Square()."""
        with self.assertRaises(TypeError):
            Square()

    def test_square_five_args(self):
        """Test Square(1, 2, 3, 4, 5)."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_square_none(self):
        """Test Square(None)."""
        with self.assertRaises(TypeError):
            Square(None)

    def test_square_float(self):
        """Test Square(1.5)."""
        with self.assertRaises(TypeError):
            Square(1.5)

    def test_str_method(self):
        """Test __str__() of Square."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_area(self):
        """Test the area method."""
        self.assertEqual(Square(5).area(), 25)

    def test_display(self):
        """Test display with and without offsets."""
        self.assertEqual(capture(Square(2).display), "##\n##\n")
        self.assertEqual(capture(Square(1, 1, 2).display), "\n\n #\n")

    def test_size_getter_setter(self):
        """Test the size getter and setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))

    def test_size_setter_errors(self):
        """Test the size setter with invalid values."""
        s = Square(5)
        with self.assertRaisesRegex(
                TypeError, "^width must be an integer$"):
            s.size = "9"
        with self.assertRaises(ValueError):
            s.size = 0

    def test_update_args(self):
        """Test update with positional arguments."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(5)
        s.update(x=12)
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        """Test that kwargs are skipped when args exist."""
        s = Square(1, 0, 0, 1)
        s.update(5, size=100)
        self.assertEqual(str(s), "[Square] (5) 0/0 - 1")

    def test_update_invalid_values(self):
        """Test that update validates values."""
        s = Square(1)
        with self.assertRaises(TypeError):
            s.update(1, "a")
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        s = Square(10, 2, 1, 7)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 7, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update(self):
        """Test that a dictionary can update another instance."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)


    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")


    def test_load_from_file(self):
        """Test Square.load_from_file() with an existing file."""
        with open("Square.json", "w") as f:
            f.write('[{"id": 4, "size": 1, "x": 2, "y": 3}]')
        out = Square.load_from_file()
        self.assertIsInstance(out[0], Square)
        self.assertEqual(str(out[0]), "[Square] (4) 2/3 - 1")


if __name__ == "__main__":
    unittest.main()
