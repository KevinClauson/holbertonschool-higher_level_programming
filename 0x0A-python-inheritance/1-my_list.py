#!/usr/bin/python3
""" module with one class """


class MyList(list):
    """ subcall of list that adds a method to print """
    def print_sorted(self):
        """prints out sorted list """
        print(sorted(self))
