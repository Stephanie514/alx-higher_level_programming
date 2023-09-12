#!/usr/bin/python3
"""Defines a module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the
    number of characters added.
    """
    try:
        with open(filename, "a", encoding="utf-8") as my_file:
            char_count = my_file.write(text)
            return char_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
