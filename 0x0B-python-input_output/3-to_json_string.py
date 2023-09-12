#!/usr/bin/python3
"""
Defines a module that returns the JSON representation
of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The Python object to be serialized to JSON.

    Returns:
        str: A JSON string representation of the input object.
    """
    json_string = json.dumps(my_obj)
    return json_string
