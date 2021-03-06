#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
import json
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests for base
    """
    def test_presence_of_module_docstring(self):
        """Presence of module docstring"""
        module_doc = base.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        """Presence of class docstring"""
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        """Presence of init docstring"""
        init_doc = Base.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_to_json_docstring(self):
        """Presence of to json docstring"""
        to_js_doc = Base.to_json_string.__doc__
        self.assertTrue(len(to_js_doc) > 1)

    def test_presence_of_from_json_docstring(self):
        """Presence of from json docstring"""
        f_js_doc = Base.from_json_string.__doc__
        self.assertTrue(len(f_js_doc) > 1)

    def test_presence_of_save_to_file_docstr(self):
        """Presence of save to file docstring"""
        stf_doc = Base.save_to_file.__doc__
        self.assertTrue(len(stf_doc) > 1)

    def test_presence_of_create_docstring(self):
        """Presence of create docstring"""
        c_doc = Base.create.__doc__
        self.assertTrue(len(c_doc) > 1)

    def test_presence_of_load_from_file_docstr(self):
        """Presence of load from file docstring"""
        lff_doc = Base.load_from_file.__doc__
        self.assertTrue(len(lff_doc) > 1)

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

    def test_to_json_string(self):
        """Test to_json_string"""
        s = [{'id': 99}, {'height': 66}]
        t = '[{"id": 99}, {"height": 66}]'
        self.assertEqual(Base.to_json_string(s), t)

    def test_to_json_string_none(self):
        """Test to_json_string when parameter is none"""
        s = None
        t = '[]'
        self.assertEqual(Base.to_json_string(s), t)
    
    def test_to_json_string_empty(self):
        """Test to_json_string when parameter is empty"""
        s = []
        t = '[]'
        self.assertEqual(Base.to_json_string(s), t)

    def test_save_to_file_none(self):
        """Test save_to_file with parameter of none"""
        Base.save_to_file(None)
        with open("Base.json", "r") as fd:
            s = json.load(fd)
            self.assertEqual(len(s), 0)
            self.assertEqual(s, [])

    def test_save_to_file_empty(self):
        """Test save_to_file with parameter empty"""
        Base.save_to_file([])
        with open("Base.json", "r") as fd:
            s = json.load(fd)
            self.assertEqual(len(s), 0)
            self.assertEqual(s, [])

    def test_load_from_file(self):
        """Test load_from_file with no file"""
        s = Base.load_from_file()
        self.assertEqual(s, [])
