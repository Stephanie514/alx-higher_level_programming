#!/usr/bin/python3
"""Unittests for Base
"""

import unittest
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


if __name__ == '__main__':
    unittest.main()
