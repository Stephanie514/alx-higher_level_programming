#!/usr/bin/python3

class Rectangle:
    """Rectangle class definition."""

    count = 0
    symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance."""
        self.set_width(width)
        self.set_height(height)
        Rectangle.count += 1

    def __str__(self):
        """Return a string representation of the Rectangle."""
        if self.get_height() == 0 or self.get_width() == 0:
            return ''

        rectangle_str = ''
        for _ in range(self.get_height()):
            for _ in range(self.get_width()):
                rectangle_str += str(self.symbol)
            rectangle_str += '\n'

        return rectangle_str[:-1]

    def __repr__(self):
        """Return a string representation to recreate the instance."""
        return "Rectangle({}, {})".format(self.get_width(), self.get_height())

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.count -= 1

    def get_width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    def set_width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    def set_height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.get_width() * self.get_height()

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        if self.get_height() == 0 or self.get_width() == 0:
            return 0
        return 2 * (self.get_width() + self.get_height())
