#!/usr/bin/python3
"""
Defines the Amenity model class.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity model class that inherits from BaseModel.

    Attributes:
        name (str): Represents the name of the Amenity.
                   Initialized to an empty string.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of Amenity.
        """
        super().__init__(*args, **kwargs)
        self.name = ''
