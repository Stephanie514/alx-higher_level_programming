#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (number): The size of the new square.
        """
        self.my_size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.my_size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.my_size = value

    def area(self):
        """Return the current area of the square."""
        return self.my_size * self.my_size

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()

    def __str__(self):
        """Define the print() representation of a Square."""
        return f"A square with size: {self.my_size}"


if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(3)
    print(square1 == square2)
    print(square1 > square2)
    print(square1 < square2)
    print(square1)
