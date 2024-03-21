#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the type of city_id."""
        new = self.value()
        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """Tests the type of amenity_ids."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
