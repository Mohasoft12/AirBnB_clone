#!/usr/bin/python3

"""
Defines the Place model class, inheriting from BaseModel.
"""

from models.base_model import BaseModel
from typing import List

class Place(BaseModel):
    """
    Represents a place entity, inheriting attributes and methods from BaseModel.

    Attributes:
        city_id (str): ID of the city associated with the place.
        user_id (str): ID of the user who owns the place.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests the place can accommodate.
        price_by_night (int): Price per night for staying at the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        amenity_ids (List[str]): List of IDs of amenities available at the place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of Place.

        Args:
            *args: Positional arguments (not used directly).
            **kwargs: Keyword arguments for initializing attributes:
                city_id (str): ID of the city associated with the place.
                user_id (str): ID of the user who owns the place.
                name (str): Name of the place.
                description (str): Description of the place.
                number_rooms (int): Number of rooms in the place.
                number_bathrooms (int): Number of bathrooms in the place.
                max_guest (int): Maximum number of guests the place can accommodate.
                price_by_night (int): Price per night for staying at the place.
                latitude (float): Latitude coordinate of the place.
                longitude (float): Longitude coordinate of the place.
                amenity_ids (List[str]): List of IDs of amenities available at the place.
        """
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])

    def __str__(self):
        """
        Returns a string representation of the Place instance.

        Returns:
            str: String representation of the Place instance.
        """
        return f"[Place] ({self.id}) {self.name}, {self.city_id} ({self.number_rooms} rooms)"

    def add_amenity(self, amenity_id):
        """
        Adds an amenity ID to the list of amenity IDs.

        Args:
            amenity_id (str): ID of the amenity to add.
        """
        if amenity_id not in self.amenity_ids:
            self.amenity_ids.append(amenity_id)

    def remove_amenity(self, amenity_id):
        """
        Removes an amenity ID from the list of amenity IDs.

        Args:
            amenity_id (str): ID of the amenity to remove.
        """
        if amenity_id in self.amenity_ids:
            self.amenity_ids.remove(amenity_id)
