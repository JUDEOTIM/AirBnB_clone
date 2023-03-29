#!/usr/bin/python3
""" Test User Unittest module
"""

from datetime import datetime, date
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser_Object_instance(unittest.TestCase):

    """ Test User class instance object
    """

    def setUp(self):
        print("Testing User Object Instance")

    def test_user_is_a_sublass_basemodel(self):
        u1 = User()
        self.assertIsInstance(u1, BaseModel)

    def test_user_unique_ids(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_user_email_default_value(self):
        u1 = User()
        self.assertEqual(u1.email, "")

    def test_user_firstname_default_value(self):
        u1 = User()
        self.assertEqual(u1.first_name, "")

    def test_user_password_default_value(self):
        u1 = User()
        self.assertEqual(u1.password, "")

    def test_user_lastname_default_value(self):
        u1 = User()
        self.assertEqual(u1.last_name, "")

    def test_user_id_type(self):
        u1 = User()
        self.assertEqual(type(u1.id), str)

    def test_user_object_creation_time(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.created_at, u2.created_at)

    def test_user_firstname_attr(self):
        u1 = User()
        u1.first_name = "Ayobami"
        self.assertEqual(u1.first_name, "Ayobami")

    def test_user_lastname_attr(self):
        u1 = User()
        u1.last_name = "Al-Areef"
        self.assertEqual(u1.last_name, "Al-Areef")

    def test_user_password_attr(self):
        u1 = User()
        u1.password = "Alx"
        self.assertEqual(u1.password, "Alx")

    def test_user_email_attr(self):
        u1 = User()
        u1.email = "Alx@example.com"
        self.assertEqual(u1.email, "Alx@example.com")


class TestUser_Has_attr_basemodel(unittest.TestCase):

    """ Test User for super class attributes
    """

    def setUp(self):
        print("Testing if User has the attributes of BaseModel")

    def test_user_has_id_attr(self):
        u1 = User()
        self.assertTrue(u1.id)

    def test_user_has_created_at_attr(self):
        u1 = User()
        self.assertTrue(u1.created_at)

    def test_user_has_updated_at_attr(self):
        u1 = User()
        self.assertTrue(u1.updated_at)

    def test_user_can_take_kwargs(self):
        u2 = User(name="Al-Areef")
        self.assertEqual(u2.name, "Al-Areef")

    def test_user_can_take_multiple_kwargs(self):
        u2 = User(name="Al-Areef", partner="Ayobami")
        self.assertEqual(u2.partner, "Ayobami")

    def test_user_object_str_representation(self):
        u1 = User()
        self.assertIn("[User]", u1.__str__())


if __name__ == "__main__":
    unittest.main()
