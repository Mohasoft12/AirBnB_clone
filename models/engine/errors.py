#!/usr/bin/python3

"""
Defines custom exceptions for file storage operations.
"""

class ModelNotFoundError(Exception):
    """Exception raised when a model is not found."""
    def __init__(self, model_name="BaseModel"):
        super().__init__(f"Model with name '{model_name}' is not registered!")


class InstanceNotFoundError(Exception):
    """Exception raised when an instance is not found."""
    def __init__(self, obj_id="", model="BaseModel"):
        super().__init__(f"Instance of '{model}' with id '{obj_id}' does not exist!")
