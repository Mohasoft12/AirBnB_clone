#!/usr/bin/python3

"""
Definition of the BaseModel class, the foundation for our models.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models, providing common functionality.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        If kwargs are provided, initializes from serialized data.
        Otherwise, initializes with new data and stores in models.storage.

        Args:
            *args: Positional arguments (not used directly).
            **kwargs: Keyword arguments for initializing attributes.
        """
        if kwargs:
            self.deserialize(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def deserialize(self, data):
        """
        Deserializes data and initializes instance attributes.

        Args:
            data (dict): Dictionary containing serialized data.
        """
        if '__class__' in data:
            del data['__class__']
        for key, value in data.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute and saves the instance to storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        data = self.__dict__.copy()
        data['__class__'] = type(self).__name__
        data['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        data['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return data

    @classmethod
    def all(cls):
        """
        Retrieves all instances of cls from storage.

        Returns:
            list: List of instances of cls.
        """
        return models.storage.all(cls)

    @classmethod
    def count(cls):
        """
        Retrieves the count of instances of cls.

        Returns:
            int: Number of instances of cls.
        """
        return models.storage.count(cls)

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new instance of cls and saves it to storage.

        Returns:
            str: ID of the newly created instance.
        """
        instance = cls(**kwargs)
        instance.save()
        return instance.id

    @classmethod
    def show(cls, instance_id):
        """
        Retrieves an instance of cls by its ID.

        Args:
            instance_id (str): ID of the instance to retrieve.

        Returns:
            instance: Instance of cls if found, None otherwise.
        """
        return models.storage.find(cls, instance_id)

    @classmethod
    def destroy(cls, instance_id):
        """
        Deletes an instance of cls by its ID.

        Args:
            instance_id (str): ID of the instance to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return models.storage.delete(cls, instance_id)

    @classmethod
    def update(cls, instance_id, **kwargs):
        """
        Updates an instance of cls by its ID with new attributes.

        Args:
            instance_id (str): ID of the instance to update.
            **kwargs: Keyword arguments containing attributes to update.
        """
        instance = cls.show(instance_id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
        else:
            print("** no instance found **")

