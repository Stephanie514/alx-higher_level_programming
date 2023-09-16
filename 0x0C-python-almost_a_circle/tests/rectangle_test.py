#!/usr/bin/python3
"""
Unittests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


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


if __name__ == '__main__':
    unittest.main()
