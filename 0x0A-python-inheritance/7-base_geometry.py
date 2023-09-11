#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Base class for geometric calculations."""

    def area(self):
        """Calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, attribute, value):
        """Validate an integer value."""
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute} must be greater than 0")
