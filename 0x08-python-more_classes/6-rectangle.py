#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Define a Rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the Rectangle (default is 0).
            height (int, optional): The height of the Rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a string representation of the Rectangle using '#'.

        Returns:
            str: A string representing the Rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ''
        rect_str = ''
        for i in range(self.height):
            rect_str += '#' * self.width
            if i < self.height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """
        Returns a string representation of the Rectangle for eval().

        Returns:
            str: A string representation of the Rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes a Rectangle instance and prints a message."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Retrieves the width of a Rectangle instance.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of a Rectangle instance.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
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

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of a Rectangle instance.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a Rectangle instance.

        Returns:
            int: The area of the Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of a Rectangle instance.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
