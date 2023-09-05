#!/usr/bin/python3
"""Define 9-rectangle
"""


class Rectangle:
    """Rectangle class definition.
    """

    count = 0
    symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance in a constructor.
        """
        self.__width = width
        self.__height = height
        Rectangle.count += 1

    def __str__(self):
        """Returns an informal string representation.
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rect_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += str(self.symbol)
            if i < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """Return an internal string representation of a Rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Fires when a rectangle is destroyed."""
        print("Bye rectangle...")
        Rectangle.count -= 1

    def get_width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    def set_width(self, value):
        """Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    def set_height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size
        """
        return cls(size, size)
