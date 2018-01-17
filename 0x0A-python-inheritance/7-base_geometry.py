#!/usr/bin/python3
""" module with one class """


class BaseGeometry:
    """ class that is having functionality added piece by piece """
    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks value """
        if not type(value) == int:
            raise TypeError('{} must be an integer'.format(name)) 
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
