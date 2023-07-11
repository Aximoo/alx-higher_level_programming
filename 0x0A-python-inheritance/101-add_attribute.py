#!/usr/bin/python3
"""Defines a function that addss attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute too an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name oof the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
