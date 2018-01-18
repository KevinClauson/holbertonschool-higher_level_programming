#!/usr/bin/python3
""" module with one function """


def append_write(filename="", text=""):
    """function that write to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
