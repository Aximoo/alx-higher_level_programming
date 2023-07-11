#!/usr/bin/python3
"""
function that creates an Objeect from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """crate and object fromm a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
