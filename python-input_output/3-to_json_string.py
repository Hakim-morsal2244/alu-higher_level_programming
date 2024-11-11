#!/usr/bin/python3

"""
This module contains a function that returns the JSON representation
of an object. It uses the `json.dumps()` method to serialize an object
into a JSON-formatted string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        A string containing the JSON representation of the object.
    """
    try:
        return json.dumps(my_obj)
    except TypeError:
        raise TypeError("Object of type set is not JSON serializable")
