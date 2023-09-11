#!/usr/bin/python3
"""Check if an object is an instance of a class that inherited
(directly or indirectly) from a specified class."""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class; otherwise, False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.

    Returns:
        bool: True if obj is an instance of a class that inherits from a_class
(directly or indirectly); otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
