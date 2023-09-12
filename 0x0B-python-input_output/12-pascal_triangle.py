#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for current_row_number in range(n):
        current_row = [1]  # First element is always 1

        if triangle:
            previous_row = triangle[-1]
            for i in range(len(previous_row) - 1):
                current_element = previous_row[i] + previous_row[i + 1]
                current_row.append(current_element)

            current_row.append(1)  # Last element is always 1

        triangle.append(current_row)

    return triangle
