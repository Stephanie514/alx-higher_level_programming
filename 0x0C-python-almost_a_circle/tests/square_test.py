#!/usr/bin/python3
"""Unittest for square class
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test square class"""

    def setUp(self):
        """Set up for all methods"""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test if Square class initializes with correct values"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_update(self):
        """Test the update method to assign values to attributes"""
        s1 = Square(3)
        s1.update(89, 3)
        self.assertEqual(s1.width, 3)

    def test_str(self):
        """Test the __str__ method"""
        s1 = Square(5)
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), expected_output)

    def test_size_validation(self):
        """Test size validation in Square class"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(-5)

    def test_x_validation(self):
        """Test x-coordinate validation in Square class"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(5, -1)

    def test_y_validation(self):
        """Test y-coordinate validation in Square class"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1 = Square(5, 1, -2)

    def test_to_dictionary(self):
        """Test the to_dictionary method to return dictionary"""
        s1 = Square(10, 2, 1)
        expected_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_dict)

    def test_size_getter(self):
        """Test the size getter method"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_setter(self):
        """Test the size setter method"""
        s1 = Square(5)
        s1.size = 8
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, 8)


if __name__ == '__main__':
    unittest.main()
