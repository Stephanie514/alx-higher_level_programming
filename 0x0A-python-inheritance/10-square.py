#!/usr/bin/python3

""" Define square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class body """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square side.
        """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
