#!/usr/bin/python3
""" module with one class that inhierts from int """

class MyInt(int):
        def __eq__(self, other):
            #print "A __eq__ called: %r == %r ?" % (self, other)
            return int(self) != other
     
        def __ne__(self, other):
            """ change not equal to equal """
            return int(self) == other
