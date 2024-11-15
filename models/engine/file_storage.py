#!/usr/bin/python3
"""Defines the file storage class for the hbnb clone"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Reprsent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {k: obj.to_dict() for k, o in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objects_dict = json.load(f)
                for key, val in objects_dict.items():
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
