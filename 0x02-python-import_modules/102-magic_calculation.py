#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub
    c = 0 if a < b else sub(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c
