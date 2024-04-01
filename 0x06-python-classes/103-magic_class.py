#!/usr/bin/python3
"""To perform a byte code operation"""

import math


class MagicClass:
    """The class of Magicclass"""

    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        return math.pi * (self._MagicClass__radius ** 2)

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
