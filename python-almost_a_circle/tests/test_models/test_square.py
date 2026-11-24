#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
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

    def tearDown(self):
        """Remove files created by the tests."""
        for n in ("Square.json", "Rectangle.json"):
            if os.path.exists(n):
                os.remove(n)

    def test_1(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y), (1, 0, 0))

    def test_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.x, s.y), (2, 0))

    def test_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.x, s.y), (2, 3))

    def test_1_2_3_4(self):
        """Test Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_str_size(self):
        """Test Square("1")."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_str_x(self):
        """Test Square(1, "2")."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_str_y(self):
        """Test Square(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_neg_size(self):
        """Test Square(-1)."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_neg_x(self):
        """Test Square(1, -2)."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_neg_y(self):
        """Test Square(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero(self):
        """Test Square(0)."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_method(self):
        """Test __str__() for Square."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (4) 2/3 - 1")

    def test_area_display(self):
        """Test area() and display() of Square."""
        self.assertEqual(Square(2).area(), 4)
        self.assertEqual(capture(Square(2).display), "##\n##\n")

    def test_size_setter(self):
        """Test the size getter and setter."""
        s = Square(1)
        s.size = 4
        self.assertEqual((s.size, s.width, s.height), (4, 4, 4))
        with self.assertRaises(TypeError):
            s.size = "1"

    def test_to_dictionary(self):
        """Test to_dictionary() in Square."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(),
                         {"id": 4, "size": 1, "x": 2, "y": 3})

    def test_update_none(self):
        """Test update() in Square."""
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_update_89(self):
        """Test update(89) in Square."""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Square."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Square."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Square."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89}) in Square."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_size(self):
        """Test update(**{'id': 89, 'size': 1}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_x(self):
        """Test update(**{'id': 89, 'size': 1, 'x': 2}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_y(self):
        """Test update with id, size, x and y in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test Square.create(**{'id': 89})."""
        self.assertEqual(Square.create(**{'id': 89}).id, 89)

    def test_create_size(self):
        """Test Square.create(**{'id': 89, 'size': 1})."""
        self.assertEqual(Square.create(**{'id': 89, 'size': 1}).size, 1)

    def test_create_x(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_y(self):
        """Test Square.create with id, size, x and y."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertEqual(Base.from_json_string(f.read()),
                             [{"id": 1, "size": 1, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        """Test Square.load_from_file() when the file does not exist."""
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test Square.load_from_file() when the file exists."""
        with open("Square.json", "w") as f:
            f.write('[{"id": 4, "size": 1, "x": 2, "y": 3}]')
        self.assertEqual(str(Square.load_from_file()[0]),
                         "[Square] (4) 2/3 - 1")


if __name__ == "__main__":
    unittest.main()
