#!/usr/bin/python3
"""This defines module appends a string."""


def append_write(filename="", text=""):
    """This appends string to the end of a UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as file_to_append:
        return file_to_append.write(text)
