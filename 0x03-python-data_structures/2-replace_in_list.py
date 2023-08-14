#!/usr/bin/python3

# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    result = my_list[:]

    if 0 <= idx < len(result):
        result.pop(idx)
        result.insert(idx, element)

    return result
