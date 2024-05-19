#!/usr/bin/python3
"""
Defines the State class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Represents a state with a name attribute.
    """
    def __init__(self, name: str = ''):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"State: {self.name}"
