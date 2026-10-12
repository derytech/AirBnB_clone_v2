#!/usr/bin/python3
"""Defines the Amenity class."""

from sqlalchemy import Column, String
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an Amenity."""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False, default="")
