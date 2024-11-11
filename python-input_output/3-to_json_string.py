#!/usr/bin/python3


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    # Convert set to list if the object is a set
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    return json.dumps(my_obj)
