#!/usr/bin/python3

# 9-max_integer.py

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        result = None
    else:
        max_value = max(my_list)
        result = max_value
    return result
