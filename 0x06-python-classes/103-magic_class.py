import math

"""Define MagicClass matching given bytecode"""


class MagicClass:
    """Represent the area circle"""
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__r = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__r = radius

    def compute_area(self):
        return self.__r ** 2 * math.pi

    def compute_circumference(self):
        return 2 * math.pi * self.__r
