#!/usr/bin/python3

""" Define base_geometry module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class body """

    def __init__(self, rect_width, rect_height):
        """
        Initializes a Rectangle instance.

        Args:
            rect_width (int): The width of the rectangle.
            rect_height (int): The height of the rectangle.
        """
        super().integer_validator("width", rect_width)
        super().integer_validator("height", rect_height)
        self.__width = rect_width
        self.__height = rect_height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
