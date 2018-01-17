#!/usr/bin/python3
""" module with one class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class that inherits from Rectangle"""
    def __init__(self, size):
        """instantiate with width and height """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area """
        return self.__size * self.__size

    def __str__(self):
        """ width and height of square """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)