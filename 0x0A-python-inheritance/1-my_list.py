#!/usr/bin/python3
"""MyList: A custom list class inheriting from the built-in list class."""


class MyList(list):
    """MyList is an extension of the list class with more functionality."""

    def print_sorted(self):
        """Prints the list in ascending order after sorting."""
        sorted_list = sorted(self)
        print(sorted_list)
