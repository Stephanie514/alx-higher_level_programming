#!/usr/bin/python3

# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    div_by_2 = [num % 2 == 0 for num in my_list]
    return div_by_2
