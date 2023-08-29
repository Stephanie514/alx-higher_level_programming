#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent a class square"""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self._Square__size = 0  # Initialize the private attribute
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """Return the current area of the square."""
        return self.size ** 2
