#!/usr/bin/python3

# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if 0 <= idx < len(my_list):
        new_copy = my_list[:]
        new_copy[idx] = element
        return new_copy
    return my_list
