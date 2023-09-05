#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')

    for line in lines:
        line = line.strip()
        if line.endswith(('.', '?', ':')):
            print(line)
            print()
        else:
            print(line)
