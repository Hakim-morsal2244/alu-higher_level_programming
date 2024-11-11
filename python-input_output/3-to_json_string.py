#!/usr/bin/python3

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
    except TypeError as e:
        raise TypeError(f"{my_obj} is not JSON serializable") from e
