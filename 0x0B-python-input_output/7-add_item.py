#!/usr/bin/python3
"""Script to add command-line arguments to a Python
list and save to a file."""

import sys
from json_utils import (
    save_to_json_file as save_json,
    load_from_json_file as load_json
)

if __name__ == "__main__":
    try:
        argument_list = load_json("arguments.json")
    except FileNotFoundError:
        argument_list = []

    argument_list.extend(sys.argv[1:])
    save_json(argument_list, "arguments.json")
