#!/usr/bin/python3
""" Unit Test for 'Rectangle' class """


import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class test_base(unittest.TestCase):

    def test_parent(self):
        """ Test for parent class value """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instantiate(self):
        """ Test instantiation """
        with (self.assertRaises(TypeError)):
            rectangle1 = Rectangle()

        rectangle2 = Rectangle(1, 2)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 0)
        self.assertEqual(rectangle2.y, 0)

        rectangle3 = Rectangle(9, 8, 7, 6, 98)
        self.assertEqual(rectangle3.width, 9)
        self.assertEqual(rectangle3.height, 8)
        self.assertEqual(rectangle3.x, 7)
        self.assertEqual(rectangle3.y, 6)
        self.assertEqual(rectangle3.id, 98)

    def test_errors(self):
        """ Test for error triggers """
        with (self.assertRaises(TypeError)):
            rectangle4 = Rectangle("1", 2)
        with (self.assertRaises(TypeError)):
            rectangle4 = Rectangle(3, [4])
        with (self.assertRaises(TypeError)):
            rectangle4 = Rectangle("5", "6")
        with (self.assertRaises(TypeError)):
            rectangle4 = Rectangle(7)
        with (self.assertRaises(ValueError)):
            rectangle4 = Rectangle(2, 0)
        with (self.assertRaises(ValueError)):
            rectangle4 = Rectangle(0, 3)
        with (self.assertRaises(ValueError)):
            rectangle4 = Rectangle(1, 2, 0, -1)
        with (self.assertRaises(ValueError)):
            rectangle4 = Rectangle(1, 2, -10, 10)

    def test_area(self):
        """ Test 'Rectangle' class' public 'area' function """
        rectangle5 = Rectangle(5, 6, 7, 8, 100)
        self.assertEqual(rectangle5.area(), 30)

    def test_display(self):
        """ Test 'Rectangle' class' public 'display' function """
        rectangle6 = Rectangle(2, 3)
        sys.stdout = StringIO()
        rectangle6.display()
        self.assertEqual(sys.stdout.getvalue(), "##\n##\n##\n")
        sys.stdout = sys.__stdout__

    def test_str_overload(self):
        """ Test output for overloading '__str__' """
        rectangle7 = Rectangle(4, 5, 6, 7, 101)
        sys.stdout = StringIO()
        print(rectangle7)
        self.assertEqual(sys.stdout.getvalue(),
                         "[Rectangle] (101) 6/7 - 4/5\n")
        sys.stdout = sys.__stdout__

    def test_display_1(self):
        """ Test 'Rectangle' class' public 'display' function """
        rectangle8 = Rectangle(3, 2, 2, 2)
        sys.stdout = StringIO()
        rectangle8.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n  ###\n  ###\n")
        sys.stdout = sys.__stdout__

    def test_update(self):
        """ Test 'Rectangle' class' public 'update' function """
        rectangle9 = Rectangle(1, 1, 1, 1)
        rectangle9.update(55, 4, 3, 2, 1)
        self.assertEqual(rectangle9.id, 55)
        self.assertEqual(rectangle9.width, 4)
        self.assertEqual(rectangle9.height, 3)
        self.assertEqual(rectangle9.x, 2)
        self.assertEqual(rectangle9.y, 1)

        rectangle10 = Rectangle(2, 2, 2, 2)
        rectangle10.update(width=1, x=9, height=7, y=8, id=56)
        self.assertEqual(rectangle10.id, 56)
        self.assertEqual(rectangle10.width, 1)
        self.assertEqual(rectangle10.height, 7)
        self.assertEqual(rectangle10.x, 9)
        self.assertEqual(rectangle10.y, 8)
