#!/usr/bin/python3

"""
This file defines the storage system for the project.
It uses JSON format to serialize and deserialize objects.
"""

import json
from json.decoder import JSONDecodeError
from datetime import datetime
from .errors import ModelNotFoundError, InstanceNotFoundError
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serves as an object-relational mapping interface for database operations.
    """

    _models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self, file_path='file.json'):
        """
        Initializes FileStorage with a file path.
        """
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
        Returns all objects stored in __objects dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects and saves it to a JSON file.
        """
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes JSON file and loads objects into __objects.
        """
        try:
            with open(self.__file_path, "r") as f:
                serialized = json.load(f)
                self.__objects = {
                    key: self._models[obj['__class__']](**obj) for key, obj in serialized.items()
                }
        except (FileNotFoundError, JSONDecodeError):
            pass  # File doesn't exist or JSON decoding error

    def find_by_id(self, model_name, obj_id):
        """
        Finds and returns an object by its model name and ID.
        """
        if model_name not in self._models:
            raise ModelNotFoundError(f"Model '{model_name}' not found.")
        
        key = f"{model_name}.{obj_id}"
        if key not in self.__objects:
            raise InstanceNotFoundError(f"Instance of '{model_name}' with id '{obj_id}' not found.")

        return self.__objects[key]

    def delete_by_id(self, model_name, obj_id):
        """
        Deletes an object by its model name and ID.
        """
        if model_name not in self._models:
            raise ModelNotFoundError(f"Model '{model_name}' not found.")
        
        key = f"{model_name}.{obj_id}"
        if key not in self.__objects:
            raise InstanceNotFoundError(f"Instance of '{model_name}' with id '{obj_id}' not found.")

        del self.__objects[key]
        self.save()

    def find_all(self, model_name=None):
        """
        Finds and returns all objects of a given model_name.
        If model_name is None, returns all objects.
        """
        if model_name and model_name not in self._models:
            raise ModelNotFoundError(f"Model '{model_name}' not found.")

        results = []
        for key, obj in self.__objects.items():
            if not model_name or key.startswith(f"{model_name}."):
                results.append(obj)

        return results

    def update_one(self, model_name, obj_id, field, value):
        """
        Updates a specific field of an object identified by model_name and obj_id.
        """
        if model_name not in self._models:
            raise ModelNotFoundError(f"Model '{model_name}' not found.")

        key = f"{model_name}.{obj_id}"
        if key not in self.__objects:
            raise InstanceNotFoundError(f"Instance of '{model_name}' with id '{obj_id}' not found.")

        instance = self.__objects[key]
        if hasattr(instance, field):
            setattr(instance, field, value)
            instance.updated_at = datetime.utcnow()
            self.save()
        else:
            raise AttributeError(f"Field '{field}' not found in instance.")

