#!/usr/bin/python3
"""Defines an integer addition function."""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero.

    Returns:
        list: A new matrix representing the result of the division.

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        result.append(new_row)
    
    return result
