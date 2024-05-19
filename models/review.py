#!/usr/bin/python3

"""
Defines the Review model class, inheriting from BaseModel.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review entity, inheriting attributes and methods from BaseModel.

    Attributes:
        place_id (str): ID of the place associated with the review.
        user_id (str): ID of the user who wrote the review.
        text (str): Content of the review text.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of Review.

        Args:
            *args: Positional arguments (not used directly).
            **kwargs: Keyword arguments for initializing attributes:
                - place_id (str): ID of the place associated with the review.
                - user_id (str): ID of the user who wrote the review.
                - text (str): Content of the review text.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

    def __str__(self):
        """
        Returns a string representation of the Review instance.

        Returns:
            str: String representation of the Review instance.
        """
        return f"[Review] ({self.id}) User {self.user_id} on Place {self.place_id}: {self.text[:50]}"
