#!/usr/bin/python3
# 0-safe_print_list.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
