#!/usr/bin/python3

"""
This module defines the MagicClass which represents a circle.
"""

import math


class MagicClass:
    """
    The MagicClass represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def compute_area(self):
        """
        Compute the area of the circle.

        Returns:
            float: The computed area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def compute_circumference(self):
        """
        Compute the circumference of the circle.

        Returns:
            float: The computed circumference of the circle.
        """
        return 2 * math.pi * self.__radius
