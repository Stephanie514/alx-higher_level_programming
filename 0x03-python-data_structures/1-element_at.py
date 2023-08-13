#!/usr/bin/python3

# 1-element_at.py

def element_at(my_list, idx):
    """Retrieve an element from a list."""
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None
