#!/usr/bin/python3
"""class MagicClass"""
import math


class MagicClass:
    """reps a circle"""
    def __init__(x, radius=0):
        """Initializes Magic Class"""
        x.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        x.__radius = radius

    def area(x):
        """Calculaes area of circle"""
        return (x.__radius ** 2) * math.pi

    def circumference(x):
        """Calculates circumference of circle"""
        return 2 * math.pi * x.__radius
