#!/usr/bin/python3

# 9-max_integer.py

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return None

    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num

    return biggest
