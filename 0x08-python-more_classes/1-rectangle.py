#!/usr/bin/python3
"""
module with class that defines rectange
"""


class Rectangle:
    """ Represents a rectangle """
    def __init__(self, width=0, height=0):
        """ init a rectangle with width and height """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ method that return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter that sets the height and checks if int """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """ return the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width and checks for int and negatives """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
