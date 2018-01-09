#!/usr/bin/python3
"""
module with one function that defines a rectangle
"""


class Rectangle:
    """ Represents a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init a rectangle with width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    s += str(self.print_symbol)
                s += '\n'
        return s

    def __repr__(self):
        """ prints out string version of rectangle """
        s = "Rectangle("
        s += str(self.__width)
        s += ", "
        s += str(self.__height)
        s += ")"
        return s

    def __del__(self):
        """ detects deletion of REctangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle…")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
