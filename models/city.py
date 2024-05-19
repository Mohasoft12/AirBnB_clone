#!/usr/bin/python3

"""
Defines the City model class, inheriting from BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city entity, inheriting attributes and methods from BaseModel.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.

        Args:
            *args: Positional arguments (not used directly).
            **kwargs: Keyword arguments for initializing attributes:
                - state_id (str): The state ID associated with the city.
                - name (str): The name of the city.
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')

    def __str__(self):
        """
        Returns a string representation of the City instance.

        Returns:
            str: String representation of the City instance.
        """
        return f"[City] ({self.id}) {self.name} in {self.state_id}"
