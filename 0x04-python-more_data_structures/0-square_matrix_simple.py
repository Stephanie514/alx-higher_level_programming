#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = [[0] * len(row) for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
