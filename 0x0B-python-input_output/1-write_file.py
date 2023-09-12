#!/usr/bin/python3
"""Defines WriteFile module."""


def write_file(file_name="", content=""):
    """Write a string to a UTF-8 text file and return the character count."""
    try:
        with open(file_name, "w", encoding="utf-8") as my_file:
            my_file.write(content)
            char_count = len(content)
            return char_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
