#!/usr/bin/python3
"""
Test module with unit tests for class Rectangle
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    check ID
    """
    def test_rec_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r3 = Rectangle(15, 5)
        self.assertEqual(r3.id, 3)

    def test_str_prints_a_square(self):
        """ Checks that __str__ prints correct representation of a Square """
        x = Square(2)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('##\n##\n', output.getvalue())