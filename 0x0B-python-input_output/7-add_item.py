#!/usr/bin/python3
"""Script to add command-line arguments to a Python list and
save them to a JSON file."""

import sys
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Loads an object from a JSON file."""
    try:
        with open(filename, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    filename = "add_item.json"
    items = load_from_json_file(filename)
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
