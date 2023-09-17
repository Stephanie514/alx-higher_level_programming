#!/usr/bin/python3
"""
This module defines the Base class for managing IDs.
"""

import json
import csv
import turtle


class Base:
    """
    The Base class for managing ID attributes.

    Attributes:
        __nb_objects (int): A private class attribute to count objects.
        id (int): A public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new object with a unique ID.

        Args:
            id (int, optional): The ID for the object. Defaults to None.

        Attributes:
            id (int): The unique ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
