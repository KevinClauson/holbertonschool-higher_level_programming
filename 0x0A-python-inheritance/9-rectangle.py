#!/usr/bin/python3
""" module with one class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeo"""
    def __init__(self, width, height):
        """instantiate with width and height """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def __str__(self):
        """ width and height of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
