#!/usr/bin/python3
"""Student class definition."""


class Student:
    """Represents a student."""

    def __init__(self, first, last, years):
        """Initialize student attributes."""
        self.first_name = first
        self.last_name = last
        self.age = years

    def to_json(self, attributes=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attributes (list): A list of attribute names to include in the dictionary.

        Returns:
            dict: A dictionary containing the specified attributes and their values.
        """
        if attributes is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attributes}

    def reload_from_json(self, json_data):
        """
        Replace all attributes of the Student instance from a dictionary.

        Args:
            json_data (dict): A dictionary containing attribute names and their values.
        """
        for key, value in json_data.items():
            setattr(self, key, value)

