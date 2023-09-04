#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Rectangle class defined by width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of a Rectangle instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of a Rectangle instance.

        Args:
            value (int): The width value, must be a positive integer.
                         Raises:
                           - TypeError: if width is not an integer.
                           - ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of a Rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of a Rectangle instance.

        Args:
            value (int): The height value, must be a positive integer.
                         Raises:
                           - TypeError: if height is not an integer.
                           - ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
