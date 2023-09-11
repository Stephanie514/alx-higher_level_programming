#!/usr/bin/python3
"""This function returns a list of attributes and methods of an object."""


def lookup(obj):
    """Return a list of attributes and methods available for the object."""
    return dir(obj)
