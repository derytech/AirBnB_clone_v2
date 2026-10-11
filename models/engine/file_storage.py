#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return all objects, optionally filtered by class."""
        if cls is None:
            return self.__objects

        filtered_objects = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                filtered_objects[key] = obj

        return filtered_objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def delete(self, obj=None):
        """Delete an object from the storage dictionary."""
        if obj is None:
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def save(self):
        """Serialize all objects to the JSON file."""
        objects_dict = {}

        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to the storage dictionary."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objects_dict = json.load(file)

            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }

            for key, obj_dict in objects_dict.items():
                class_name = obj_dict.get("__class__")

                if class_name in classes:
                    self.__objects[key] = classes[class_name](**obj_dict)

        except FileNotFoundError:
            pass
