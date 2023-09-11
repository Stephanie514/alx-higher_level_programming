#!/usr/bin/python3
"""Check if an object is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the
    specified class; otherwise, False.

    Args:
        obj (any): Object to check.
        a_class (type): The class to compare the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
