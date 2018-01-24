#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests for base
    """

    def test_ids(self):
        """Testing correct ids"""
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

if __name__ == "__main__":
    unittest.main()
