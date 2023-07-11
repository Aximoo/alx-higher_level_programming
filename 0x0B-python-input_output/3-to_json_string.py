#!/usr/bin/python3
"""
contain the JSON striing
"""

import json


def to_json_string(my_obj):
    """returns the JSON repressentation of an object (string)"""
    return json.dumps(my_obj)
