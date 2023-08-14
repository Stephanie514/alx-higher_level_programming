#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, element in enumerate(row):
            if idx < len(row) - 1:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element))
        if not row:
            print()
