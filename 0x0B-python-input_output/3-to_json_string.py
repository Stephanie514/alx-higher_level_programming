#!/usr/bin/python3
"""Defines a module that returns the JSON representation
of an object (string)."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    try:
        import json
        return json.dumps(my_obj)
    except TypeError as e:
        return f"[{e.__class__.__name__}] {str(e)}"
