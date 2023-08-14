#!/usr/bin/python3

# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    if len(tuple_a) == 0:
        new_tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        new_tuple_a = tuple_a[0], 0
    
    if len(tuple_b) == 0:
        new_tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        new_tuple_b = tuple_b[0], 0

    result_tuple = (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])
    return result_tuple
