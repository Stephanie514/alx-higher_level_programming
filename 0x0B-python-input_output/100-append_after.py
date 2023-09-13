#!/usr/bin/python3
"""
This module defines a function append_after that inserts a line of text into
a file after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file after each line
containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after lines
containing the search_string.
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
