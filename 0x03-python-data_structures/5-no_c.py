#!/usr/bin/python3

# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    filtered_chars = [char for char in my_string if char.lower() != 'c']
    return "".join(filtered_chars)
