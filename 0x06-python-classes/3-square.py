#!/usr/bin/python3

"""class Square."""


class Square:
    """Represent square."""

    def __init__(x, size=0):
        """Initializes a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        x.__size = size

    def area(x):
        """Return current area square."""
        return (x.__size * x.__size)
