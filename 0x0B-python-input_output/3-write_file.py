#!/usr/bin/python3
""" module with one function """


def write_file(filename="", text=""):
    """function that write to a file"""
    char_count = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
