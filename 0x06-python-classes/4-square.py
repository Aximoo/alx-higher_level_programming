#!/usr/bin/python3

"""class Square."""


class Square:
    """ square."""

    def __init__(x, size=0):
        """Initialize a new square
        """
        x.size = size

    @property
    def size(x):
        """set size square."""
        return (x.__size)

    @size.setter
    def size(x, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        x.__size = value

    def area(x):
        """Return current area square."""
        return (x.__size * x.__size)
