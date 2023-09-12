#!/usr/bin/python3
"""
read_file.py

This script defines a function to read a text file
(UTF-8) and print it to stdout.
"""


def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                print(chunk, end='')
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./read_file.py filename")
    else:
        read_file(sys.argv[1])
