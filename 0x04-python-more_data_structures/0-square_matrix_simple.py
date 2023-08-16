#!/usr/bin/pythoet3

def square_matrix_simple(matrix_input=[]):
    result_matrix = matrix_input.copy()

    for row_index in range(len(matrix_input)):
        original_row = matrix_input[row_index]
        squared_row = list(map(lambda value: value ** 2, original_row))
        result_matrix[row_index] = squared_row

    return result_matrix
