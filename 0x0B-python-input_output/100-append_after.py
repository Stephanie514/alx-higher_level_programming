#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line
containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line to insert after lines
containing the search_string.
    """
    result = []
    with open(filename, "r") as file:
        for line in file:
            result.append(line)
            if search_string in line:
                result.append(new_string)

    with open(filename, "w") as file:
        file.writelines(result)
