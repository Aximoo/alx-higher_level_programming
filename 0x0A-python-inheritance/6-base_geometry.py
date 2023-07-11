#!/usr/bin/python3
"""
Contains the class BaaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an eexception when called"""
        raise Exception("area() is not implemented")
