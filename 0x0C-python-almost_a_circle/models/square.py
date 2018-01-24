#!/usr/bin/python3
"""
    module with class Squares
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiates a square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        pretty print of square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
            Getter for width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Setter for width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updat values of Square
        """
        numargs = len(args)
        if numargs:
            self.id = args[0]
            if numargs > 1:
                self.size = args[1]
            if numargs > 2:
                self.x = args[2]
            if numargs > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.width = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
