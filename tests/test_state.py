#!/usr/bin/python3
""" Test User Unittest module
"""

from datetime import datetime, date
import unittest
from models.user import User
from models.base_model import BaseModel
from models.state import State


class TestState_Object_instance(unittest.TestCase):

    """ Test User class instance object
    """

    def setUp(self):
        print("Testing State Object Instance")

    def test_State_is_a_sublass_basemodel(self):
        s1 = State()
        self.assertIsInstance(s1, BaseModel)

    def test_state_unique_ids(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_state_name_default_value(self):
        s1 = State()
        self.assertEqual(s1.name, "")

    def test_state_id_type(self):
        s1 = State()
        self.assertEqual(type(s1.id), str)

    def test_state_object_creation_time(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_state_name_attr(self):
        s1 = State()
        s1.name = "Lagos"
        self.assertEqual(s1.name, "Lagos")

    def test_state_name(self):
        s1 = State()
        self.assertEqual(s1.name, "")


class TestState_Has_attr_basemodel(unittest.TestCase):

    """ Test User for super class attributes
    """

    def setUp(self):
        print("Testing if State has the attributes of BaseModel")

    def test_state_has_id_attr(self):
        s1 = State()
        self.assertTrue(s1.id)

    def test_state_has_created_at_attr(self):
        s1 = State()
        self.assertTrue(s1.created_at)

    def test_state_has_updated_at_attr(self):
        s1 = State()
        self.assertTrue(s1.updated_at)

    def test_state_can_take_kwargs(self):
        s2 = State(name="Al-Areef")
        self.assertEqual(s2.name, "Al-Areef")

    def test_state_can_take_multiple_kwargs(self):
        s2 = State(name="Al-Areef", partner="Ayobami")
        self.assertEqual(s2.partner, "Ayobami")

    def test_state_object_str_representation(self):
        s1 = State()
        self.assertIn("[State]", s1.__str__())


if __name__ == "__main__":
    unittest.main()
