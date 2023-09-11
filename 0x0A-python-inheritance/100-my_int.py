#!/bin/usr/python3
"""Class that inherits from int"""


class MyInt(int):
    """MyInt class body"""

    def __eq__(self, other):
        """Override == operator with !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with =="""
        return super().__eq__(other)
