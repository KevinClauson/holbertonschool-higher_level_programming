#!/usr/bin/python3
""" 
module that contains a func that adds two ints
"""


def add_integer(a, b):
    """ func that adds a and b """
    try:
        return int(a) + int(b)
    except (TypeError, ValueError):
        print("a must be an integer")
    