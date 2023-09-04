#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a Rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with specified width and height.

        Args:
            width (int, optional): The width of the Rectangle (default is 0).
            height (int, optional): The height of the Rectangle (default is 0).
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def get_width(self):
        """
        Get the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self._width

    def set_width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def get_height(self):
        """
        Get the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self._height

    def set_height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    width = property(get_width, set_width)
    height = property(get_height, set_height)
