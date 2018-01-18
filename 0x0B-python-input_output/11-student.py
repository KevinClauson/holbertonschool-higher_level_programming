#!/usr/bin/python3
"""module with one class"""


class Student:
    """class that defines student"""
    def __init__(self, first_name, last_name, age):
        """instantiaon"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict"""
        return self.__dict__
