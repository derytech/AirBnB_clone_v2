#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel:
    """Defines common attributes and methods for other classes."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        table = getattr(self.__class__, "__table__", None)

        if table is not None:
            for column in table.columns:
                if column.default is not None and column.default.is_scalar:
                    setattr(self, column.name, column.default.arg)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key in ("created_at", "updated_at"):
                if isinstance(value, str):
                    value = datetime.fromisoformat(value)
            setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the timestamp and save the object."""
        from models import storage

        self.updated_at = datetime.utcnow()

        if self.__class__.__name__ == "BaseModel":
            return

        storage.new(self)
        storage.save()
    def delete(self):
        """Delete the current instance from storage."""
        from models import storage

        storage.delete(self)

    def to_dict(self):
        """Return a dictionary of instance attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

