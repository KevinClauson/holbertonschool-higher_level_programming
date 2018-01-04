#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ instantization of size and position """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ returns the position var"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position, checks if tuple, length of 2 int less than 0"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) != int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[1]) != int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ returns the squared area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square at the position"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for p in range(0, self.__position[0]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
