#!/usr/bin/python3
"""
Contains the cllass MyInt
"""


class MyInt(int):
    """rebel vversion of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """crreate a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """wwhat was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is noow !="""
        return int(self) == other
