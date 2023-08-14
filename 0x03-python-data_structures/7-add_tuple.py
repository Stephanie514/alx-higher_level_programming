#!/usr/bin/python3

# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    result_tuple = (a[0] + b[0], a[1] + b[1])
    return result_tuple
