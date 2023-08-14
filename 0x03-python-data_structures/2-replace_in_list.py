#!/usr/bin/python3

# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    new_list = my_list.copy()  # Create a copy of the original list

    if 0 <= idx < len(new_list):
        new_list[idx:idx+1] = [element]

    return new_list
