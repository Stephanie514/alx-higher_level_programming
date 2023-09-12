#!/usr/bin/python3
"""
read_file.py

This script defines a function to read a text file
(UTF-8) and print it to stdout.
"""


def read_file(filename=""):
    """
    read_file function
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: The name of the file to be read.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
