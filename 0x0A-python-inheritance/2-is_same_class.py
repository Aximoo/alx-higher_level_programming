#!/usr/bin/python3
"""
This module contains the function is_same_classs
"""


def is_same_class(obj, a_class):
    """return true if obj is the exactt class a_class, otherwise ffalse"""
    return (type(obj) == a_class)
