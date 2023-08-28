#!/usr/bin/python3
def raise_exception():
    try:
        1 + '1'
    except TypeError:
        raise TypeError("A custom type exception has been raised")
