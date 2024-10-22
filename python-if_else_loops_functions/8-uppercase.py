#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")
    print()  # Print a new line at the end
