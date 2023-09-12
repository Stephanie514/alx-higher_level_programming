#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


def class_to_json(obj):
    """ Returns a dictionary description of the object
for JSON serialization.
    """
    return obj.__dict__


if __name__ == "__main__":
    obj = MyClass("example")
    json_description = class_to_json(obj)
    print(json_description)
