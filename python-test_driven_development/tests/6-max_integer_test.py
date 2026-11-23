#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered(self):
        """Test ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max at beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty(self):
        """Test empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative(self):
        """Test all negative numbers."""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_floats(self):
        """Test floats and mixed."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_same(self):
        """Test all same values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_no_arg(self):
        """Test no argument returns None."""
        self.assertIsNone(max_integer())
