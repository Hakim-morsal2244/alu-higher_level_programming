#!/usr/bin/python3
# File: 100-main.py

MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)         # Expected output: 3
print(my_i == 3)    # Expected output: False (inverted equality)
print(my_i != 3)    # Expected output: True (inverted inequality)
