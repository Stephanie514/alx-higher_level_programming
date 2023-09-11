#!/usr/bin/python3
"""Check if an object is an inherited instance of a specified class."""


def is_kind_of_class(obj, target_class):
    """Return True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise, False.

    Args:
        obj (any): The object to check.
        target_class (type): The class to compare the type of obj to.

    Returns:
        bool: True if obj is an instance of target_class or a subclass;
        otherwise, False.
    """
    return isinstance(obj, target_class)
