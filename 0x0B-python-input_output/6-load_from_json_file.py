#!/usr/bin/python3

"""Module for loading Python objects from JSON files."""

import json


def load_from_json_file(file_name):
    """
    Load a Python object from a JSON file.

    Args:
        file_name (str): The name of the JSON file to read from.

    Returns:
        obj: The Python object loaded from the JSON file.
    """
    with open(file_name, encoding="utf-8") as json_file:
        loaded_obj = json.load(json_file)
        return loaded_obj
