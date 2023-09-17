#!/usr/bin/python3
"""Unittests for Base
"""

import unittest
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unit tests for Base model"""

    def test_initialization(self):
        """Test if Base class initializes with unique IDs"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id_assignment(self):
        """Test if Base class assigns custom IDs correctly"""
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string(self):
        """Test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(
            Base.to_json_string([{'id': 1, 'name': 'Alice'}]),
            '[{"id": 1, "name": "Alice"}]'
        )

    def test_save_to_file(self):
        """Test save_to_file method"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(
                content,
                json.dumps([
                    {"id": 1, "width": 10, "height": 5, "x": 0, "y": 0},
                    {"id": 2, "width": 7, "height": 3, "x": 0, "y": 0}
                ])
            )

        Base._Base__nb_objects = 0

        s1 = Square(6)
        s2 = Square(8)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(
                content,
                json.dumps([
                    {"id": 1, "size": 6, "x": 0, "y": 0},
                    {"id": 2, "size": 8, "x": 0, "y": 0}
                ])
            )


if __name__ == '__main__':
    unittest.main()
