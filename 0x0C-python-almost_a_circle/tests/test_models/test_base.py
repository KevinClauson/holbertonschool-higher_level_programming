#!/usr/bin/python3
"""
Test module with unit tests for class Base
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_ids(self):
        """Test ids"""
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.b6 = Base(15)
        self.b7 = Base()
        self.b8 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, 15)
        self.assertEqual(self.b7.id, 5)
        self.assertEqual(self.b8.id, 6)

if __name__ == "__main__":
    unittest.main()