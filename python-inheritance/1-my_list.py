#!/usr/bin/python3

class MyList(list):
    """
    MyList class inherits from the built-in list.
    It includes a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
