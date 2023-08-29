#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.my_size = size
        self.my_position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.my_size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.my_size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.my_position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.my_position = value

    def area(self):
        """Return the current area of the square."""
        return self.my_size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.my_size == 0:
            print("")
            return

        for _ in range(self.my_position[1]):
            print()
        for _ in range(self.my_size):
            print(" " * self.my_position[0] + "#" * self.my_size)


if __name__ == "__main__":
    my_square = Square()
    my_square.my_size = int(input("Enter the size of the square: "))
    my_square.my_position = tuple(
        map(int, input("Enter the position of the square (x, y): ").split())
    )
    print("Square size:", my_square.size)
    print("Square position:", my_square.position)
    print("Square area:", my_square.area())
    my_square.my_print()
