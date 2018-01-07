#!/usr/bin/python3
"""
module with one function that prints name
"""


def say_my_name(first_name, last_name=""):
    """ function that prints name """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
    else:
        if isinstance(first_name, str):
            raise TypeError("last_name must be a string")
        else:
            raise TypeError("first_name must be a string")
