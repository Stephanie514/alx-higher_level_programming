#!/usr/bin/python3
"""
Unittests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


class TestRectangle(unittest.TestCase):
    """Define unit tests for Rectangle class"""

    def test_initialization(self):
        """Test if Rectangle class initializes with correct values"""
        r1 = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 10)

    def test_width_validation(self):
        """Test width validation in Rectangle class"""
        with self.assertRaises(TypeError):
            r2 = Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)

    def test_height_validation(self):
        """Test height validation in Rectangle class"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(4, "invalid")
        with self.assertRaises(ValueError):
            r5 = Rectangle(4, 0)

    def test_x_validation(self):
        """Test x-coordinate validation in Rectangle class"""
        with self.assertRaises(TypeError):
            r6 = Rectangle(4, 5, "invalid")
        with self.assertRaises(ValueError):
            r7 = Rectangle(4, 5, -1)

    def test_y_validation(self):
        """Test y-coordinate validation in Rectangle class"""
        with self.assertRaises(TypeError):
            r8 = Rectangle(4, 5, 1, "invalid")
        with self.assertRaises(ValueError):
            r9 = Rectangle(4, 5, 1, -2)

    def test_valid_inputs(self):
        """Test valid input values"""
        r1 = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 10)

        r2 = Rectangle(10, 20)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_invalid_combinations(self):
        """Test different combinations of valid and invalid inputs"""
        with self.assertRaises(TypeError):
            r3 = Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 5)

        with self.assertRaises(TypeError):
            r5 = Rectangle(4, "invalid")
        with self.assertRaises(ValueError):
            r6 = Rectangle(4, 0)

        with self.assertRaises(TypeError):
            r7 = Rectangle(4, 5, "invalid")
        with self.assertRaises(ValueError):
            r8 = Rectangle(4, 5, -1)

        with self.assertRaises(TypeError):
            r9 = Rectangle(4, 5, 1, "invalid")
        with self.assertRaises(ValueError):
            r10 = Rectangle(4, 5, 1, -2)

    def test_area(self):
        """Test the area method to calculate the area of a rectangle."""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.area(), 20)

    def test_display(self):
        """Test the display method to print the Rectangle instance."""
        r1 = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###\n"

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        """Test the __str__ method to check the string representation."""
        r1 = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(r1), expected_str)


if __name__ == '__main__':
    unittest.main()
