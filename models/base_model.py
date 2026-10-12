#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

from models import storage
from models.engine.db_storage import Base
from sqlalchemy import Column, DateTime, String


class BaseModel(Base):
    """Defines common attributes and methods for other classes."""

    __abstract__ = True

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the updated_at attribute and save the object."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all instance attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
