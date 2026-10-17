#!/usr/bin/python3
"""Defines the User class."""

import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Defines a User."""

    __tablename__ = "users"

    email = Column(String(128), nullable=False, default="")
    password = Column(String(128), nullable=False, default="")
    first_name = Column(String(128), nullable=True, default="")
    last_name = Column(String(128), nullable=True, default="")

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship(
            "Place",
            back_populates="user",
            cascade="all, delete, delete-orphan"
        )
