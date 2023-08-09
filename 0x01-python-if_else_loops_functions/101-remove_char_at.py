#!/usr/bin/python3

# 101-remove_char_at.py

def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    result = ""
    for i in range(len(str)):
        if i != n:
            result += str[i]
    return result
