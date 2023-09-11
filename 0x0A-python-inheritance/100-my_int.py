#!/usr/bin/python3
""" Define MyInt class that inherits from int."""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted."""

    def __eq__(self, other):
        """Override == operator with !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with =="""
        return super().__eq__(other)
