#!/usr/bin/python3
"""
module with one function that prints a square
"""

def print_square(size):
    """ prints square given a size """
    if isinstance(size, float) and i < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end='')
            print()
