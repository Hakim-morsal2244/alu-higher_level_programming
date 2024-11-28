#!/usr/bin/python3
"""
Unit tests for Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class.
    """

    def test_width_type(self):
        """Test width type validation."""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_height_type(self):
        """Test height type validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, "5")

    def test_width_value(self):
        """Test width value validation."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    def test_height_value(self):
        """Test height value validation."""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_x_type(self):
        """Test x type validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "1", 2)

    def test_y_type(self):
        """Test y type validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 1, "2")

    def test_x_value(self):
        """Test x value validation."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1, 2)

    def test_y_value(self):
        """Test y value validation."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 1, -2)
