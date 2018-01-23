#!/usr/bin/python3
"""
module for Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    class rectangle inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of Rec
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def setter_check(var, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(var))
        elif (var == "x" or var == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(var))
        elif (var == "width" or var == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(var))

    @property
    def width(self):
        """
        Getter for the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        self.setter_check("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_check("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x 

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.setter_check("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        self.setter_check("y", value)
        self.__y = value

    def area(self):
        """
        return area of rect
        """
        return self.__width *self.__height

    def display(self):
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}".format(self.__x * " "), end='')
            print("{}".format(self.__width * '#'))

    def __str__(self):
        """
        pretty print of rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height) 

    def update(self, *args, **kwargs):
        """
        Updat values of Rectangle
        """
        numargs = len(args)
        if numargs:
            self.id = args[0]
            if numargs > 1:
                self.width = args[1]
            if numargs > 2:
                self.height = args[2]
            if numargs > 3:
                self.x = args[3]
            if numargs > 4:
                self.x = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "width" in kwargs:
                self.width = kwargs.get("width")
            if "height" in kwargs:
                self.height = kwargs.get("height")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
    
    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
