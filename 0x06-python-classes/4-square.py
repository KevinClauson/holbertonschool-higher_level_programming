#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ instantization of size """
        self.size = size

    @property
    def size(self):
        """ returns the size var"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size variable checking if int or less than 0"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the squared area of square"""
        return self.__size ** 2
