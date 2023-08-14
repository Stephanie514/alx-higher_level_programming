#!/usr/bin/python3

# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        for a in reversed(my_list):
            print("{:d}".format(a))
