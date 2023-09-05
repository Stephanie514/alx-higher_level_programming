#!/usr/bin/python3

"""Defines a square-printing function."""


def print_square(size):
    """
    Print a square with the '#' character.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        row = "#" * size
        print(row)
