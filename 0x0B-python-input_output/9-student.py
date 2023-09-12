#!/usr/bin/python3
"""Student Class Definition"""


class Student:
    """Defines a student with basic information."""

    def __init__(self, first, last, age):
        """Initialize student attributes.

        Args:
            first (str): The first name of the student.
            last (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first
        self.last_name = last
        self.student_age = age

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.student_age
        }
