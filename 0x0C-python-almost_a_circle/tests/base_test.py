#!/usr/bin/python3
"""Unittests for Base
"""

import unittest
import json
import io  # Added import for 'io'
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import os


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

    def test_from_json_string(self):
        """Test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(
            Base.from_json_string('[{"id": 1, "name": "Alice"}]'),
            [{'id': 1, 'name': 'Alice'}]
        )

    def test_create(self):
        """Test create method"""
        r = Rectangle.create(id=99)
        self.assertEqual(r.id, 99)

        s = Square.create(id=42)
        self.assertEqual(s.id, 42)

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_load_from_file(self):
        """Test load_from_file method"""
        filename = "Rectangle.json"
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        Rectangle.save_to_file([r1, r2])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, 10)
        self.assertEqual(loaded_rectangles[1].height, 3)

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        Rectangle.save_to_file_csv([r1, r2])

        with open("Rectangle.csv", "r") as file:
            content = sorted(file.read().strip().split('\n'))
            expected = sorted("id,width,height,x,y\n1,10,5,0,0\n2,7,3,0,0".split('\n'))
            self.assertEqual(content, expected)

        s1 = Square(6)
        s2 = Square(8)
        Square.save_to_file_csv([s1, s2])

        with open("Square.csv", "r") as file:
            content = sorted(file.read().strip().split('\n'))
            expected = sorted("id,size,x,y\n1,6,0,0\n2,8,0,0".split('\n'))
            self.assertEqual(content, expected)

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        Rectangle.save_to_file_csv([r1, r2])

        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles), 2)

        s1 = Square(6)
        s2 = Square(8)
        Square.save_to_file_csv([s1, s2])

        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)

    def test_draw(self):
        """Test the draw method."""
        r1 = Rectangle(50, 30)
        r2 = Rectangle(100, 50)
        s1 = Square(40)
        s2 = Square(80)

        list_rectangles = [r1, r2]
        list_squares = [s1, s2]

        with unittest.mock.patch('builtins.input', return_value="click"):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                Base.draw(list_rectangles, list_squares)

        self.assertIn("click", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
