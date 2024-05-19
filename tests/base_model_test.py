#!/usr/bin/env python3
"""
Unit tests for BaseModel and related classes.
"""

import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_attributes_types(self):
        """Test types of BaseModel attributes."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.my_number, int)

    def test_save_method_updates_updated_at(self):
        """Test if save method updates updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary with correct keys and formats."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str_representation(self):
        """Test string representation of BaseModel instance."""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


class TestModels(unittest.TestCase):
    """Unit tests for related models: State, City, Amenity, Review."""

    def test_state_model(self):
        """Test State model attributes."""
        state = State()
        state.name = "Kenya"
        self.assertEqual(state.name, "Kenya")

    def test_city_model(self):
        """Test City model attributes."""
        state_id = uuid4()
        city = City()
        city.name = "Nairobi"
        city.state_id = state_id
        self.assertEqual(city.name, "Nairobi")
        self.assertEqual(city.state_id, state_id)

    def test_amenity_model(self):
        """Test Amenity model attributes."""
        amenity = Amenity()
        amenity.name = "Free Wifi"
        self.assertEqual(amenity.name, "Free Wifi")

    def test_review_model(self):
        """Test Review model attributes."""
        place_id = uuid4()
        user_id = uuid4()
        review = Review()
        review.place_id = place_id
        review.user_id = user_id
        review.text = "Good"
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, "Good")


if __name__ == "__main__":
    unittest.main()

