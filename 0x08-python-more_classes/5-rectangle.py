#!/usr/bin/python3
"""
module with one function that defines a rectangle
"""


class Rectangle:
    """ Represents a rectangle """
    def __init__(self, width=0, height=0):
        """ init a rectangle with width and height """
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            s += '\n'
            return s
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    s += '#'
                s += '\n'
        return s

    def __repr__(self):
        s = "Rectangle("
        s += str(self.__width)
        s += ", "
        s += str(self.__height)
        s += ")"
        return s

    def __del__(self):
        print("Bye rectangle…")
