#!/usr/bin/python3
# 1-my_list.py
class MyList(list):
    def print_sorted(self):
        """Prints the list, but sorted (ascending order) without modifying the original list."""
        print(sorted(self))

