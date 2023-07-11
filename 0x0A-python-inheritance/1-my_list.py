#!/usr/bin/python3
"""
contains the MyLiist class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the obbject"""
        super().__init__()

    def print_sorted(self):
        """prints the sortedd list"""
        print(sorted(self))
