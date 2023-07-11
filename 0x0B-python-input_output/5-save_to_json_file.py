#!/usr/bin/python3
"""
function that writes an Object to a teext file
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, ussing a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
