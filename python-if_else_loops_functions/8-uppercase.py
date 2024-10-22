#!/usr/bin/python3

def uppercase(str):

    """Print a string in uppercase followed by a new line."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if character is lowercase
            c = chr(ord(c) - 32)  # Convert to uppercase
        print("{}".format(c), end="")
    print()  # New line at the end
