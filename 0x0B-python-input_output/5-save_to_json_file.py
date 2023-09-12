#!/usr/bin/python3

"""Module for saving Python objects to JSON files."""

import json


def save_to_json_file(obj, file_name):
    """
    Save a Python object to a JSON file.

    Args:
        obj: The Python object to be saved.
        file_name (str): The name of the JSON file to write to.
    """
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(obj, json_file, ensure_ascii=False)
