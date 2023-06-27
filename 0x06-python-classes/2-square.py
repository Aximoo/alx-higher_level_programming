#!/usr/bin/python3
""" defines square """


class Square:
    """ square """

    def __init__(self, x=0):
        """
        size square
        """

        if type(x) is int:
            if x < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__x = x
        else:
            raise TypeError('size must be an integer')
