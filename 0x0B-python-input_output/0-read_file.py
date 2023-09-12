#!/usr/bin/python3
"""
read_file.py

This script defines a function to read a text file
(UTF-8) and print it to stdout.
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
