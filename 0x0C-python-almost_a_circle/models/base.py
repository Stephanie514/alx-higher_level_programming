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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(obj_dicts)
        filename = class_name + ".json"
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries from a JSON string representation.

        Args:
            json_string (str): A JSON string representing a
            list of dictionaries.

        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: A list of instances created from the data in the JSON file.
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                for item in json_list:
                    instance_list.append(cls.create(**item))
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances to be serialized.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w") as file:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This deserializes a list of instances from CSV file.

        Returns:
            list: A list of instances created from the data in the CSV file.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    instance_dict = {k: int(v) for k, v in row.items()}
                    instance_list.append(cls.create(**instance_dict))
        except FileNotFoundError:
            pass

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using Turtle graphics module."""
        turtle.speed(0)
        turtle.bgcolor("white")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()
