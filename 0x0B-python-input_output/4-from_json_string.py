#!/usr/bin/python3

"""Module for parsing JSON strings."""


import json


def from_json_string(json_string):
    """
    Parse a JSON string and return the corresponding Python object.

    Args:
        json_string (str): The JSON string to be parsed.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    parsed_obj = json.loads(json_string)
    return parsed_obj
