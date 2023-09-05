#!/usr/bin/python3

# 101-lazy_matrix_mul.py

"""Defines a matrix multiplication function using NumPy."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.

    Raises:
        ValueError: If m_a or m_b is empty.
        ValueError: If m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    """
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise e
