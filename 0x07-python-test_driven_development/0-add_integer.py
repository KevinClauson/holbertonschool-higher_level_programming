#!/usr/bin/python3
""" 
module that contains a func that adds two ints
"""


def add_integer(a, b):
    """ func that adds a and b """
    if isinstance(a,(int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        if isinstance(a, (int, float)):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer") 
