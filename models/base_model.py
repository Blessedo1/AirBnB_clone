#!/usr/bin/python3
"""Create a class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instantiate a new class.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in [created_at, updated_at]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """Returns the string representation of the instance"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}""".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__

        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
