#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
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

    def test_is_base(self):
        """Test that Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_ids(self):
        """Test automatic and given ids."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Test the attributes set by the constructor."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_default_position(self):
        """Test default values of x and y."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_missing_args(self):
        """Test missing and too many constructor arguments."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        """Test that attributes are not directly accessible."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_width_type_errors(self):
        """Test invalid types for width."""
        for bad in ("2", 2.5, None, [1], {}, (1,), True, float("nan")):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(
                        TypeError, "^width must be an integer$"):
                    Rectangle(bad, 1)

    def test_height_type_errors(self):
        """Test invalid types for height."""
        for bad in ("2", 2.5, None, [1], {}, (1,), True):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(
                        TypeError, "^height must be an integer$"):
                    Rectangle(1, bad)

    def test_x_type_errors(self):
        """Test invalid types for x."""
        for bad in ("2", 2.5, None, [1], {}, (1,), True):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(
                        TypeError, "^x must be an integer$"):
                    Rectangle(1, 1, bad)

    def test_y_type_errors(self):
        """Test invalid types for y."""
        for bad in ("2", 2.5, None, [1], {}, (1,), True):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(
                        TypeError, "^y must be an integer$"):
                    Rectangle(1, 1, 0, bad)

    def test_width_height_value_errors(self):
        """Test width and height that are zero or negative."""
        for bad in (0, -1, -100):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(
                        ValueError, "^width must be > 0$"):
                    Rectangle(bad, 1)
                with self.assertRaisesRegex(
                        ValueError, "^height must be > 0$"):
                    Rectangle(1, bad)

    def test_x_y_value_errors(self):
        """Test x and y that are negative."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Rectangle(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Rectangle(1, 1, 0, -1)

    def test_validation_order(self):
        """Test that width is validated before height."""
        with self.assertRaisesRegex(TypeError, "^width"):
            Rectangle("a", "b")
        with self.assertRaisesRegex(TypeError, "^height"):
            Rectangle(10, "2")

    def test_setters(self):
        """Test the getters and setters with valid values."""
        r = Rectangle(1, 1)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))
        r.x = 0
        r.y = 0
        self.assertEqual((r.x, r.y), (0, 0))

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
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_area(self):
        """Test the area method."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_with_args(self):
        """Test that area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display(self):
        """Test display without offsets."""
        self.assertEqual(capture(Rectangle(4, 2).display),
                         "####\n####\n")
        self.assertEqual(capture(Rectangle(1, 1).display), "#\n")

    def test_display_with_offsets(self):
        """Test display with x and y offsets."""
        self.assertEqual(capture(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(capture(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_display_with_args(self):
        """Test that display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)

    def test_str(self):
        """Test the string representation."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
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

    def test_update_too_many_args(self):
        """Test that extra positional arguments are ignored."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(str(r), "[Rectangle] (2) 5/6 - 3/4")

    def test_update_no_args(self):
        """Test update without arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_skip_kwargs(self):
        """Test that kwargs are skipped when args exist."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(5, width=100)
        self.assertEqual(str(r), "[Rectangle] (5) 0/0 - 1/1")

    def test_update_unknown_kwargs(self):
        """Test that unknown keyword arguments are ignored."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(foo=5)
        self.assertFalse(hasattr(r, "foo"))
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_invalid_values(self):
        """Test that update validates values."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(1, 1, -1)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(TypeError):
            r.update(y="a")

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """Test that a dictionary can be used to update another instance."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_is_copy(self):
        """Test that changing the dictionary does not change the object."""
        r = Rectangle(1, 1)
        r.to_dictionary()["width"] = 50
        self.assertEqual(r.width, 1)


if __name__ == "__main__":
    unittest.main()
