#!/usr/bin/python3

# 100-matrix_mul.py

"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists of lists")

    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a and m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a and m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    transposed_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in transposed_b] for row_a in m_a]

    return result
