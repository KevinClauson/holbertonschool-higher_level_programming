#!/usr/bin/python3
"""
Tests for Square Class
"""


import unittest
import sys
import io
from models.base import Base
from models import square
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square tests"""

    def test_print(self):
        """Test print method."""
        square = Square(5, 3, 5)
        out = io.StringIO()
        sys.stdout = out
        square.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), '\n\n\n\n\n   #####\n   #####\n   #####\n   #####\n   #####\n')

    def test_module_docstr(self):
        """
            is there a module docstring
        """
        module_d = square.__doc__
        self.assertTrue(len(module_d) > 1)

    def test_width_string(self):
        """
            Test when not an int
        """
        with self.assertRaises(TypeError):
            a = Square("1")

    def test_str_rep(self):
        """
            Tests string rep
        """
        square = Square(50, 50, 0, 100)
        out = io.StringIO()
        sys.stdout = out
        print(square)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), '[Square] (100) 50/0 - 50\n')

    def test_to_dictionary(self):
        """
            Tests to_dictionary method.
        """
        a = Square(15, 4, 3, 6)
        self.assertEqual(a.to_dictionary(), {'id': 6, 'x': 4, 'size': 15,
                                             'y': 3})

    def test_class_docstring(self):
        """
            is there docstring for class
        """
        class_docstr = Square.__doc__
        self.assertTrue(len(class_docstr) > 1)

    def test_init_docstring(self):
        """
            is there docstring for init
        """
        init_docstr = Square.__init__.__doc__
        self.assertTrue(len(init_docstr) > 1)

    def test_square_id(self):
        """
            Test the id for square
        """
        square1 = Square(2, 0, 0, 88)
        self.assertEqual(88, square1.id)

    def test_str_docstring(self):
        """
            is there docstring for str
        """
        str_doc = Square.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_size_docstring(self):
        """
            is there docstring for size
        """
        len_doc_str = Square.size.__doc__
        self.assertTrue(len(len_doc_str) > 1)

    def test_update_docstring(self):
        """
            is there docstring for update
        """
        len_update_doc = Square.update.__doc__
        self.assertTrue(len(len_update_doc) > 1)

    def test_to_dict_docstring(self):
        """
            is there docstring for to_dict
        """
        len_to_dic = Square.to_dictionary.__doc__
        self.assertTrue(len(len_to_dic) > 1)

    def test_all_valid_params(self):
        """
            Initialization tests with valid arguments
        """
        Base._Base__nb_objects = 0
        self.sq = Square(10, 3, 4, 12)
        self.assertEqual(self.sq.x, 3)
        self.assertEqual(self.sq.y, 4)
        self.assertEqual(self.sq.size, 10)

    def test_bad_size_type(self):
        """
            Initialization tests with invalid arguments
        """
        with self.assertRaises(TypeError) as cm:
            self.sq = Square("10")

    def test_bad_size_value(self):
        """
            Initialization tests with invalid arguments
        """
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(-10)

    def test_bad_x(self):
        """
            Initialization tests with invalid arguments
        """
        with self.assertRaises(TypeError) as cm:
            self.sq = Square(10, {})

    def test_bad_y(self):
        """
            Initialization tests with invalid arguments
        """
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(10, 3, -1)

    def test_area(self):
        """
            Area
        """
        Base._Base__nb_objects = 0
        sq1 = Square(6)
        sq2 = Square(5, 1, 2)
        sq3 = Square(7, 1, 7, 12)
        self.assertEqual(sq1.area(), 36)
        self.assertEqual(sq2.area(), 25)
        self.assertEqual(sq3.area(), 49)

    def test_display_at_origin(self):
        """
            Test display at origin
        """
        Base._Base__nb_object = 0
        r1 = Square(2)
        my_stdout = io.StringIO()
        sys.stdout = my_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "##\n##\n"
        self.assertEqual(expected, my_stdout.getvalue())

    def test_display_not_at_origin(self):
        """
            Test display not at origin
        """
        Base._Base__nb_object = 0
        r1 = Square(2, 1, 1, 2)
        my_stdout = io.StringIO()
        sys.stdout = my_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "\n ##\n ##\n"
        self.assertEqual(expected, my_stdout.getvalue())

    def test_str_prints_square(self):
        """
            Checks that __str__ prints correct representation of a Square
        """
        square2 = Square(2)
        output = io.StringIO()
        sys.stdout = output
        square2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('##\n##\n', output.getvalue())
