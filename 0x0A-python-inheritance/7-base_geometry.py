#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Base class for geometric calculations."""

    def area(self):
        """Calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
