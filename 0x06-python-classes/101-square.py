#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.coords = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def coords(self):
        """Get/set the current position of the square."""
        return self.__coords

    @coords.setter
    def coords(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__coords = value

    def area(self):
        """Return the current area of the square."""
        return self.size * self.size

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.coords[1]):
                print()
            for _ in range(self.size):
                print(" " * self.coords[0] + "#" * self.size)

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.size != 0:
            for _ in range(self.coords[1]):
                print()
        square_lines = [
            " " * self.coords[0] + "#" * self.size for _ in range(self.size)
        ]
        return "\n".join(square_lines)


if __name__ == "__main__":
    my_square = Square(3, (1, 2))
    print(my_square)
