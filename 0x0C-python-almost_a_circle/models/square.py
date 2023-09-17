#!/usr/bin/python3
"""
Define Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    # Class attribute to keep track of instances
    instances_count = 0

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization class props in constructor
        """
        super().__init__(size, size, x, y, id)
        self.__class__.instances_count += 1

    def __str__(self):
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    # Getter for size attr
    @property
    def size(self):
        return self.width  # height/width same for square

    # Setter for size attr
    @size.setter
    def size(self, value):
        """Setter for size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square attributes with *args and/or **kwargs
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dict of class props
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
