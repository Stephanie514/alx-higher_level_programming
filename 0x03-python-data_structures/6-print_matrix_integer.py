#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = " ".join(map(str, row))
        print(row_str)
