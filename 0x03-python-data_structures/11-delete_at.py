#!/usr/bin/python3

# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if 0 <= idx < len(my_list):
        new_list = my_list[:idx] + my_list[idx+1:]
    else:
        new_list = my_list[:]
    return new_list
