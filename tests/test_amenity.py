#!/usr/bin/python3
"""
    Test User unittest module
"""

from datetime import datetime, date
import unittest
from  models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity_object_instance(unittest.TestCase):

    """
        Test amenity class object instance
    """

    def setUp(self):
        print("Testing Amenity Object Instance")

    def test_Amenity_is_a_subclass_basemodel(self):
        a1 = Amenity()
        self.assertIsInstance(a1, BaseModel)

    def test_Amenity_is_instabce(self):
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

    def test_Amenity_two_ids(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_Amenity_three_ids(self):
        a1 = Amenity()
        a2 = Amenity()
        a3 = Amenity()
        self.assertNotEqual(a3.id, a1.id)

    def test_Amenity_created_time(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.created_at, a2.created_at)

    def test_Amenity_updated_time(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.updated_at, a2.updated_at)

    def test_Amenity_nameid_default_value(self):
        a1 = Amenity()
        self.assertEqual(a1.name, "")


class TestAmenity_Has_attr_basemodel(unittest.TestCase):
    """
        Test Amenity for basemodel attributes
    """

    def setUp(self):
        print("Testing if Amenity has the attributes of BaseModel")

    def test_Amenity_has_id_attr(self):
        a1 = Amenity()
        self.assertTrue(a1.id)

    def test_Amenity_has_created_at_attr(self):
        a1 = Amenity()
        self.assertTrue(a1.created_at)

    def test_Amenity_has_updated_at_attr(self):
        a1 = Amenity()
        self.assertTrue(a1.created_at)

    def test_Amenity_has__str___attr(self):
        a1 = Amenity()
        self.assertTrue(a1.__str__)

    def test_Amenity_has_save_attr(self):
        a1 = Amenity()
        self.assertTrue(a1.save)

    def test_Amenity_has_to_dict_attr(self):
        al = Amenity()
        self.assertTrue(al.to_dict)

    def test_Amenity_can_take_kwargs(self):
        a2 = Amenity(name="Al-Areef")
        self.assertEqual(a2.name, "Al-Areef")





if __name__ == "__main__":
    unittest.main()
