#!/usr/bin/python3
def magic_calculation(a, b):
    result = a
    for _ in range(b):
        result *= a
    return result + 98
