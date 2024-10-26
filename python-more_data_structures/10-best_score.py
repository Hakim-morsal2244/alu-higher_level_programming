#!/usr/bin/python3
# 10-best_score.py
# Brennan D Baraban <375@holbertonschool.com>


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
